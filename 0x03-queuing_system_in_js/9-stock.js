#!/usr/bin/node
// the below script connects to a Redis server
import { promisify } from "util";
import { createClient } from "redis";
import express from "express";

// Create a Redis client instance
const redisClient = createClient();

//
redisClient.on("err", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// an array listProducts containing the list of the below products
const listProducts = [
  {
    Id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4,
  },
  {
    Id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10,
  },
  {
    Id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2,
  },
  {
    Id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5,
  },
];

function transform(product) {
  const modified = {};
  modified.itemId = product.Id;
  modified.itemName = product.name;
  modified.price = product.price;
  modified.initialAvailableQuantity = product.stock;
  return modified;
}

// id as argument
// id - The id of the product
// returns an object
function getItemById(id) {
  for (const product of listProducts) {
    if (product.Id === id) {
      return transform(product);
    }
  }
  return {};
}

// get items
function getItems() {
  return listProducts.map(transform);
}

// reserve stock by id
function reserveStockById(itemId, stock) {
  const set_Async = promisify(redisClient.SET).bind(redisClient);
  return set_Async(`item.${itemId}`, stock);
}

// get current reserved stock
async function getCurrentReservedStockById(itemId) {
  const get_Async = promisify(redisClient.GET).bind(redisClient);
  const resrvedStock = await get_Async(`item.${itemId}`);
  if (resrvedStock === null) return 0;
  return resrvedStock;
}

// express app
const app = express();

// Endpoint to list all products
app.get("/list_products", (req, res) => {
  res.json(getItems());
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length > 0) {
    const stock = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - stock;
    return res.json(item);
  }
  return res.json({ status: "Product not found" });
});

// Endpoint to reserve a product by its ID
app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length === 0) {
    return res.json({ status: "Product not found" });
  }
  const prdct = await getCurrentReservedStockById(itemId);
  if (prdct >= item.initialAvailableQuantity) {
    return res.json({ status: "Not enough stock available", itemId });
  }
  await reserveStockById(itemId, Number(prdct) + 1);
  return res.json({ status: "Reservation confirmed", itemId });
});

// clear redis stock
// returns a promise that
// resolves when all reservations are cleared
function clearRedisStock() {
  const set_Async = promisify(redisClient.SET).bind(redisClient);
  return Promise.all(
    listProducts.map((item) => set_Async(`item.${item.Id}`, 0))
  );
}

// app.listen(1245);
app.listen(1245, async () => {
  await clearRedisStock();
  console.log("API available on localhost via port 1245");
});
