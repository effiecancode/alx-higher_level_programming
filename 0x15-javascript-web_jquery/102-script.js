$(document).ready(function() {
  // Add a click event handler to the button with ID 'btn_translate'
  $('#btn_translate').click(function() {
    // Get the language code entered by the user from the input field
    const languageCode = $('#language_code').val();

    // Make an AJAX GET request to the API with the language code
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function(data) {
      // Display the translation in the <div id="hello"> element
      $('#hello').text(data.hello);
    });
  });
});
