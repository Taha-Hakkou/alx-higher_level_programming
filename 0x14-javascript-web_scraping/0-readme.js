#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
