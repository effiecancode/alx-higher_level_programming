$(document).ready(function() {
    // Function to fetch and display the translation
    function fetchTranslation() {
      // Get the language code entered by the user from the input field
      const languageCode = $('#language_code').val();

      // Make an AJAX GET request to the API with the language code
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function(data) {
        // Display the translation in the <div id="hello"> element
        $('#hello').text(data.hello);
      });
    }

    // Add a click event handler to the button with ID 'btn_translate'
    $('#btn_translate').click(function() {
      fetchTranslation();
    });

    // Add a keypress event handler to the input field with ID 'language_code'
    $('#language_code').keypress(function(event) {
      // Check if the key pressed is the Enter key (key code 13)
      if (event.keyCode === 13) {
        fetchTranslation();
      }
    });
  });
  