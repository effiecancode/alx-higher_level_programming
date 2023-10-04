//  script that updates the text color of the <header> element to red (#FF0000)
// when the user clicks on the tag DIV#red_header:

$(document).ready(function() {
    $('#red_header').click(function() {
      $('header').css('color', '#FF0000');
    });
  });

// i used the jQuery $() function to select the <div> element
// with the id red_header. i then attached a click event handler
// using .click() to this selected <div>. When the <div> is clicked,
// i used .css() to update the text color of the <header> element to red (#FF0000).
