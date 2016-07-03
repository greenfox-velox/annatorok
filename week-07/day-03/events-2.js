'use strict';

// On the click of the button,
// Count the items in the list
// And display the result in the result element.

var button = document.querySelector('button');
var list = document.querySelectorAll('ul li');
var result = document.querySelector('.result');

 function count () {
   result.textContent = list.length;
 }

 button.addEventListener('click', count);
