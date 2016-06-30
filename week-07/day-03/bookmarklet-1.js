'use strict';

// Create a script that replaces every h1 headline's content
// with 'Green Fox Academy Conquers the World'.
// Create a bookmarklet that does that on any website.


var h1 = document.querySelectorAll('h1');

for (var i = 0; i < h1.length; i++) {
  h1[i].textContent = 'Green Fox Academy Conquers the World';
}

// h1.forEach(function (e) {
//   e.textContent = 'Green Fox Academy Conquers the World';
// })
