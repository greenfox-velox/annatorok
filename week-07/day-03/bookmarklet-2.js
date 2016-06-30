'use strict';

// Create a script that replaces every image
// with this: http://bit.ly/lpgreenfox
// Create a bookmarklet that does that on any website.

var img = document.querySelectorAll('img');

// for (var i = 0; i < img.length; i++) {
//   img[i].setAttribute('src','http://bit.ly/lpgreenfox');
// }

img.forEach(function(e) {
  e.setAttribute('src', 'http://bit.ly/lpgreenfox');
})
