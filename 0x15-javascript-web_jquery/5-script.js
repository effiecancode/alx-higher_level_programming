import $ from 'jquery';
$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});

// use the jQuery $() function to select the <div> element with the id "add_item".
// then attach a click event handler using .click() to this selected <div>.
// Inside the event handler, we create a new <li> element with the text "Item" using $('<li>Item</li>'),
// and then use .append() to add this new <li> element to the <ul> element with the class "my_list".
