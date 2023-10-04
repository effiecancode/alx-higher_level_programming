import $ from 'jquery';
$(document).ready(function () {
  $('#toggle_header').click(function () {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else {
      header.addClass('red');
    }
  });
});

// use the jQuery $() function to select the <div> element with the id "toggle_header".
// then attach a click event handler using .click() to this selected <div>.
// Inside the event handler, use .hasClass() to check if the <header> element has the class "red" or "green",
// and then use .removeClass() and .addClass() to toggle the class accordingly.
// If the <header> element has no class, default to adding the "red" class.
