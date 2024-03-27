#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];
let data = '';
request.get(url)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => {
    const complete = {};
    JSON.parse(data).forEach(task => {
      if (task.completed) {
        if (complete[task.userId] === undefined) {
          complete[task.userId] = 1;
        } else {
          complete[task.userId]++;
        }
      }
    });
    console.log(complete);
  });
