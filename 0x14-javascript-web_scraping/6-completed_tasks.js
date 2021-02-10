#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  const tasks = {};
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    for (const i in info) {
      if (tasks.completed === true) {
        if (!(tasks.userId in tasks)) {
          tasks[info[i].userId] = 1;
        } else {
          tasks[info[i].userId] += 1;
        }
      }
    }
    console.log(tasks);
  }
});
