#!/usr/bin/node
// this script connects to a Redis server
// and sets a new key-value pair
import { createClient } from "redis";

// Create a Redis client instance
const client = createClient();
const termination_messg = "KILL_SERVER";

// Event listener for connection errors
// when the connection to Redis does not work
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// connect to the Redis server running on the machine
client.on("connect", () => {
  console.log("Redis client connected to server");
});

// subscribe to the 'holberton school channel'
client.subscribe("holberton school channel");

// receive messages
// args: channel (string), message (string),
// and time (integer - in ms)
client.on("message", (_err, messg) => {
  console.log(messg);
  if (messg === termination_messg) {
    client.unsubscribe();
    client.quit();
  }
});
