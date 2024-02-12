#!/usr/bin/node
// computes and prints a factorial
const n = process.argv[2];
console.log(factorial(n));

function factorial (n) {
  if (isNaN(n) || n < 2) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
