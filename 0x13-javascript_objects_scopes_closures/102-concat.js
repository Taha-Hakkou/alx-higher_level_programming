#!/usr/bin/node
// concats 2 files
const [src1, src2, dst] = process.argv.slice(2, 5);
const fs = require('fs');
fs.readFile(src1, (err, data) => {
  if (err) throw err;
  fs.writeFile(dst, data, function () {});
});
fs.readFile(src2, (err, data) => {
  if (err) throw err;
  fs.appendFile(dst, data, function () {});
});
