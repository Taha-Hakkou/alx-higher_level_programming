#!/usr/bin/node
// searches the second biggest integer in the list of arguments
let first = 0;
let second = 0;
let n;
for (let i = 2; process.argv[i]; i++) {
  n = parseInt(process.argv[i]);
  if (n > first) {
    second = first;
    first = n;
  } else if (n > second) {
    second = n;
  }
}
console.log(second);
