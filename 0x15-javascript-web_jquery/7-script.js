import $ from 'jquery';
$(document).ready(function () {
  $('#character').text('Loading...');

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (data) {
      $('#character').text('Character Name: ' + data.name);
    },
    error: function () {
      $('#character').text('Error fetching character name.');
    }
  });
});

// use the jQuery $() function to select the <div> element with the id "character"
// and initially set its text to "Loading...".
// then use $.ajax() to make a GET request to the provided URL.
// Upon success, update the text of the <div> element with the character name
// retrieved from the API response.
// If there's an error, display an error message.
