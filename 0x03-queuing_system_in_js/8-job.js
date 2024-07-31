#!/usr/bin/npm dev

const createPushNotificationsJobs = (jobs, queue) => {
  // check if the jobs is an array
  if (!(jobs instanceof Array)) {
    // throw an error if the jobs is not an array
    throw new Error("Jobs is not an array");
  }
  // create a job in the queue
  // iterate over the jobs array
  for (const Informtn of jobs) {
    const job = queue.create("push_notification_code_2", Informtn);
    job
      // Event listener for when the job is enqueued
      .on("enqueue", () => {
        console.log("Notification job created:", job.id);
      })
      // Event listener for when the job is completed
      .on("complete", () => {
        console.log("Notification job", job.id, "completed");
      })
      // Event listener for when the job fails
      .on("failed", (err) => {
        console.log(
          "Notification job",
          job.id,
          " failed:",
          err.message || err.toString()
        );
      })
      .on("progress", (progress, _data) => {
        console.log("Notification job", job.id, `${progress}% complete`);
      });

    // save the job
    job.save();
  }
};

export default createPushNotificationsJobs;
