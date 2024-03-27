#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
//const id = 18;
let data = '';
request.get(url)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => {
    const count = JSON.parse(data).results
      .filter((film) => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
    console.log(count);
  });
