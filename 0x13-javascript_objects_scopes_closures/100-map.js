#!/usr/bin/node
// imports an array and computes a new array
const list = require('./100-data').list;
console.log(list);
const map = list.map((n, i) => n * i);
console.log(map);
