'use strict';

// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

var new_list = ['apple', 'banana', 'cat', 'dog'];
var list_items = document.querySelectorAll('li');

for (var i = 0; i < list_items.length; i++) {
  list_items[i].textContent = new_list[i];
}
