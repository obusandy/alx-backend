#!/usr/bin/node
// this script connects to a Redis server
// and sets a new key-value pair
import { createClient } from "redis";

// Create a Redis client instance
const client = createClient();

// Event listener for connection errors
// when the connection to Redis does not work
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toStringn());
});

// connect to the Redis server running on the machine
// console.log('Redis client connected to the server');
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// publish a messg
// args: message, time
// message: strng
// time: no
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish("holberton school channel", message);
  }, time);
};

// publish mesaages to the channel for holberton school
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
