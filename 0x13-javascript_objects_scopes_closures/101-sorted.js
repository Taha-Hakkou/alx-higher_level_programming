#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data').dict;
const myDict = {};
Object.keys(dict).forEach(
  function (key) {
    if (!Object.prototype.hasOwnProperty.call(myDict, dict[key])) {
      myDict[dict[key]] = [];
    }
    myDict[dict[key]].push(key);
  }
);
console.log(myDict);
