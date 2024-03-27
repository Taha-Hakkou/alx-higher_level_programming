#!/usr/bin/node
// prints all characters of a Star Wars movie preserving the order
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/';
let data = '';
request.get(url + 'films/' + id)
  .on('data', (chunk) => { data += chunk; })
  .on('end', () => {
    const characters = JSON.parse(data).characters;
    printCharacters(characters);
  });

function printCharacters (characters) {
  if (characters.length > 0) {
    request.get(characters[0])
      .on('data', (character) => {
        console.log(JSON.parse(character).name);
        printCharacters(characters.slice(1));
      });
  }
}
