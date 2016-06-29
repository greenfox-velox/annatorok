'use strict';

// Remove the king from the list.
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']

var asteroidList = document.querySelector('ul.asteroids');

var king = document.querySelector('li');
asteroidList.removeChild(king);

var new_list = ['apple', 'bubble', 'cat', 'green fox'];


// new_list.forEach(function (e) {
//   var create_listItems = document.createElement('li');
//   create_listItems.textContent = e;
//   asteroidList.appendChild(create_listItems);
// })

for (var i = 0; i < new_list.length; i++) {
  var create_listItems = document.createElement('li');
  asteroidList.appendChild(create_listItems);
  create_listItems.innerHTML = new_list[i];
}
