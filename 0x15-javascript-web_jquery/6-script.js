import $ from 'jquery';
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});

// use the jQuery $() function to select the <div> element with the id "update_header".
// then attach a click event handler using .click() to this selected <div>.
// Inside the event handler, we use .text() to update the text of the <header> element to "New Header!!!".
