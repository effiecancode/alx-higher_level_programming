// script that adds the class red to the <header> element
// when the user clicks on the tag DIV#red_header

$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});

// use the jQuery $() function to select the <div> element with the id "red_header".
// then attach a click event handler using .click() to this selected <div>.
// When the <div> is clicked, use .addClass() to add the class "red" to the <header> element.
