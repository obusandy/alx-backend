#!/usr/bin/npm dev
import { createQueue } from "kue";

// an array that will contain the blacklisted phone numbers
const BLACKLISTED = ["4153518780", "4153518781"];
const queue = createQueue();

// process jobs in the queue taking two args job and done
// the done callback will be called when all jobs are processed
// or when an error occurs
const sendNotification = (phoneNumber, message, job, done) => {
  // ttl number of intervals
  const ttl = 2;
  // pendingIntvls no of intervals
  let pendingIntvls = 2;
  // Send notification
  const sendInterval = setInterval(() => {
    if (ttl - pendingIntvls <= ttl / 2) {
      job.progress(ttl - pendingIntvls, ttl);
    }
    if (BLACKLISTED.includes(phoneNumber)) {
      // report error when phone number is blacklisted
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      // stop sending notifications
      clearInterval(sendInterval);
      return; // return from the function
    }
    if (ttl === pendingIntvls) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`
      );
    }
    --pendingIntvls || done();
    pendingIntvls || clearInterval(sendInterval);
  }, 1000); // 1 second interval
};

// Process jobs in the queue
queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
