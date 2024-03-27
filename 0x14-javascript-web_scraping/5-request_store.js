#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
let data = '';
request.get(url)
  .on('data', function (chunk) { data += chunk; })
  .on('end', async function () {
    fs.writeFile(file, data.toString(), 'utf8', (err) => {
      if (err) throw err;
    });
  });
