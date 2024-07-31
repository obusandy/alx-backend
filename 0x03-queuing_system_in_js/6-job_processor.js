#!/usr/bin/npm dev
// Create a queue with Kue
import { createQueue } from "kue";

// Create a queue with Kue
const queue = createQueue();

// below function named sendNotification
// takes two arguments phoneNumber and message
// phoneNumber: string
// message: string
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}`,
    "with message:",
    message
  );
};

// process jobs in the queue taking two args job and done
queue.process("push_notification_code", (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
