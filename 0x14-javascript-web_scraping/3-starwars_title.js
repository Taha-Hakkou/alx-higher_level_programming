#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
let data = '';
request.get(url + movieId)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => { console.log(JSON.parse(data).title); });
