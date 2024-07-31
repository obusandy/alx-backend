#!/usr/bin/node
import { promisify } from "util";
import { createClient } from "redis";
import { createQueue } from "kue";
import express from "express";

// reservationEnabled(global variable)
// the function will be executed by Kue
let reservationEnabled;
// Create a Redis client instance
const redisClient = createClient();

// Event listener for Redis connection errors
redisClient.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// Event listener for Redis connection errors
function reservSeat(number) {
  return redisClient.SET("available_seats", number);
}

// get current available seats function
// will be executed by Kue
function getCurrentAvailableSeats() {
  const get_Async = promisify(redisClient.GET).bind(redisClient);
  return get_Async("available_seats");
}

// Kue queue
const queue = createQueue();

// express app
const app = express();

app.get("/available_seats", (req, res) => {
  getCurrentAvailableSeats()
    .then((seats) => {
      res.json({ numberOfAvailableSeats: seats });
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json(null);
    });
});

// reserve a seat function
// returns the job id
app.get("/reserve_seat", (req, res) => {
  if (reservationEnabled === false) {
    return res.json({ status: "Reservation are blocked" });
  }
  const job = queue.create("reserve_seat", { task: "reserve a seat" });
  job
    .on("complete", (status) => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on("failed", (err) => {
      console.log(
        `Seat reservation job ${job.id} failed: ${
          err.message || err.toString() // in case of error
        }`
      );
    })
    .save((err) => {
      if (err) return res.json({ status: "Reservation failed" });
      return res.json({ status: "Reservation in process" });
    });
});

// process queue
app.get("/process", (req, res) => {
  res.json({ status: "Queue processing" });
  queue.process("reserve_seat", async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;
    reservSeat(availableSeats);
    if (availableSeats >= 0) {
      if (availableSeats === 0) reservationEnabled = false;
      done(); // call done when job is processed
    }
    done(new Error("Not enough seats available"));
  });
});

// port listener for API
app.listen(1245, () => {
  reservSeat(50);
  reservationEnabled = true;
  console.log("API available on localhost via port 1245");
});
