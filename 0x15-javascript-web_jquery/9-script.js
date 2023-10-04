// Use jQuery to make an AJAX GET request to the translation url
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
  // Update the content of <div id="hello"> with the transaltion
  $('#hello').text(data.hello);
});
