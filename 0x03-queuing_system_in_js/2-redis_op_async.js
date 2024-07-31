#!/usr/bin/node
// this script connects to a Redis server
// and sets a new key-value pair
import { createClient, print } from "redis";
import { promisify } from "util";

// Create a Redis client instance
const client = createClient();

// Event listener for connection errors
// when the connection to Redis does not work
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// connect to the Redis server running on the machine
client.on("connect", async () => {
  console.log("Redis client connected to the server");
  await main();
});

// accepts two arguments schoolName, and value
// schoolName - The key to set in the Redis store.
// value - The value to set in the Redis store.
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print); // prints: OK
};

// accepts one argument schoolName.
// schoolName - The key to retrieve from the Redis store.
const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  // Display the value of 'Holberton' key
  await displaySchoolValue("Holberton");
  // Set the value of 'HolbertonSanFrancisco' key to '100'
  setNewSchool("HolbertonSanFrancisco", "100");
  // Display the value of 'HolbertonSanFrancisco' key
  await displaySchoolValue("HolbertonSanFrancisco");
}
