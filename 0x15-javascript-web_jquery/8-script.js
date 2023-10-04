// Use jQuery to make an AJAX GET request to the SWAPI URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  // Get the array of movies from the response data
  const movies = data.results;

  // Iterate thru the movies and append each title to the <ul id="list_movies">
  for (const movie of movies) {
    const title = movie.title;
    $('#list_movies').append(`<li>${title}</li>`);
  }
});
