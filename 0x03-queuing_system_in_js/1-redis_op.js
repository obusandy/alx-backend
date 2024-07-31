#!/usr/bin/node
// this script connects to a Redis server
// and sets a new key-value pair
import { createClient, print } from "redis";

// Create a Redis client instance
const client = createClient();

// Event listener for connection errors
// when the connection to Redis does not work
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// connect to the Redis server running on your machine
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// schoolName - The key to set in the Redis store.
// value - The value to set in the Redis store.
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// schoolName - The key to retrieve from the Redis store.
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};
// call the functions displaySchoolValue and setNewSchool
displaySchoolValue("Holberton");
// call the functions setNewSchool
setNewSchool("HolbertonSanFrancisco", "100");
// call the functions displaySchoolValue
displaySchoolValue("HolbertonSanFrancisco");
