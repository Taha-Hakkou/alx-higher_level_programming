#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
let data = '';
request.get(url)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => {
    const n = JSON.parse(data).results
      .reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0);
    console.log(n);
  });
