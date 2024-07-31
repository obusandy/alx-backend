#!/usr/bin/node
// this script connects to a Redis server
// and sets a new key-value pair
// displays the object stored in Redis
import { createClient, print } from "redis";

// Create a Redis client instance
const client = createClient();

// Event listener for connection errors
// when the connection to Redis does not work
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// connect to the Redis server running on the machine
client.on("connect", () => {
  console.log("Redis client connected to the server");
  main();
});

// hset - stores field/value
const setCurrentHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

// display the object stored in Redis
const setHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

// main point of entry
// It stores multiple field-value pairs in a hash
// and prints the hash values
function main() {
  const hashkeyobjt = {
    portland: 50,
    Seattle: 80,
    "New York": 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashkeyobjt)) {
    setCurrentHash("HolbertonSchools", field, value);
  }
  setHash("HolbertonSchools"); // named HolbertonSchools
}
