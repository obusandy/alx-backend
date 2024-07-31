#!/usr/bin/node
// sets up a redis client
// logs a connection status messg
import { createClient } from "redis";

// Create a Redis client instance
const client = createClient();

// error messg
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// connect messg
client.on("connect", () => {
  console.log("Redis client connected to the server");
});
