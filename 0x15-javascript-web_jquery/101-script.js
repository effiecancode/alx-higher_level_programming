$(document).ready(function() {
    // Add a new <li> element to UL.my_list when DIV#add_item is clicked
    $('#add_item').click(function() {
      const newItem = $('<li>Item</li>');
      $('ul.my_list').append(newItem);
    });

    // Remove the last <li> element from UL.my_list when DIV#remove_item is clicked
    $('#remove_item').click(function() {
      const listItems = $('ul.my_list li');
      if (listItems.length > 0) {
        listItems.last().remove();
      }
    });

    // Clear all <li> elements from UL.my_list when DIV#clear_list is clicked
    $('#clear_list').click(function() {
      $('ul.my_list').empty();
    });
  });
