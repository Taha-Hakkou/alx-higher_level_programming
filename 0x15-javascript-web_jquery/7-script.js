// fetches the character name from the provided URL
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, (character) => {
  $('DIV#character').text(character.name);
});
