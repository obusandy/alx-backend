#!/usr/bin/node

import { createQueue } from "kue";
import chai from "chai";
import sinon from "sinon";
import createPushNotificationsJobs from "./8-job";

const expect = chai.expect;

const queue = createQueue();

const jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
];

describe("createPushNotificationsJobs", () => {
  beforeEach(() => {
    sinon.spy(console, "log");
  });

  // Enter Kue's test mode
  before(() => {
    queue.testMode.enter();
  });

  // Clear the queue after each test
  afterEach(() => {
    sinon.restore();
    queue.testMode.clear();
  });

  // Exit Kue's test mode after all tests have run
  after(() => {
    queue.testMode.exit();
  });

  // Test cases
  // throws an error if the jobs arg is not an array
  it("should throw an error if the jobs arg is not an array", () => {
    expect(() => createPushNotificationsJobs(1, queue)).to.throw();
    expect(() => createPushNotificationsJobs(1, queue)).to.throw(
      /Jobs is not an array/
    );
  });

  // throws an error if arg queue is not a valid kue
  it("should throw an error if arg queue is not a valid kue", function () {
    expect(() => createPushNotificationsJobs(jobs, "")).to.throw();
  });

  // logtest the creation of jobs
  it("should correctly logtest the creation of jobs", () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(
      console.log.calledOnceWith(
        `Notification job created: ${queue.testMode.jobs[0].id}`
      )
    ).to.be.true;
  });

  // log the correct job progress evnt report
  it("should correctly log job progress event report", (done) => {
    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].addListener("progress", () => {
      const id = queue.testMode.jobs[0].id;
      expect(console.log.calledWith(`Notification job ${id} 50% complete`)).to
        .be.true;
      done();
    });
    queue.testMode.jobs[0].emit("progress", 50, 100);
  });

  // log he correct job failure reort
  it("should correctly log a test job failed event report", (done) => {
    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].addListener("failed", () => {
      const id = queue.testMode.jobs[0].id;
      expect(
        console.log.calledWith(`Notification job ${id} failed: job failed!`)
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit("failed", new Error("job failed!"));
  });

  // log the correct job completion evnt
  it("should correctly log job completion events", (done) => {
    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs[0].addListener("complete", () => {
      const id = queue.testMode.jobs[0].id;
      expect(console.log.calledWith(`Notification job ${id} completed`)).to.be
        .true;
      done();
    });
    queue.testMode.jobs[0].emit("complete", true);
  });
});
