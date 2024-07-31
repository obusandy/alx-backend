#!/usr/bin/npm dev
// the below script sets up a job queue using Kue
// to be used for push notifications
import { createQueue } from "kue";

// create a queue using
const queue = createQueue({ name: "push_notification_code" });

// create a job in the queue
const job = queue.create("push_notification_code", {
  phoneNumber: "+25457005238", // the phone number to send the messg
  message: "This is the code 1934 to verify your account", // the messg to send
});

job
  .on("enqueue", () => {
    console.log("Notification job created:", job.id); // the id
  })
  .on("complete", () => {
    console.log("Notification job completed"); // the id
  })
  .on("failed attempt", () => {
    console.log("Notification job failed"); // the id
  });

// save the job
job.save();
