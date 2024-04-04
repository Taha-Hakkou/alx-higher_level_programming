// fetches and lists the title for all movies by using the provided URL
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
  const movies = data.results;
  movies.forEach((movie) => {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
