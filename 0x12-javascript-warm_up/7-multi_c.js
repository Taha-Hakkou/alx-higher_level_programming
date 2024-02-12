#!/usr/bin/node
// prints x times “C is fun”
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('C is fun');
  }
}
