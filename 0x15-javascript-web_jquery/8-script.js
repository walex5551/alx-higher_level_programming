$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data) {
    for (const movie of data.results) {
      $('ul#list_movies').append($('<li></li>').text(movie.title));
    }
  });
});
