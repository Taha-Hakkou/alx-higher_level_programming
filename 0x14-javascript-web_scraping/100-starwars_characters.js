#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/';
let data = '';
request.get(url + 'films/' + id)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => {
    const characters = JSON.parse(data).characters;
    for (let i = 0; i < characters.length; i++) {
      request.get(characters[i])
        .on('data', (data) => { console.log(JSON.parse(data).name); });
    }
  });
