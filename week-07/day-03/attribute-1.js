'use strict';

// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var img_url = document.querySelector('img');
console.log(img_url.getAttribute('src'));

img_url.setAttribute('src', 'https://avatars0.githubusercontent.com/u/7419692?v=3&s=460');

var link = document.querySelector('a');
link.getAttribute('href');
link.setAttribute('href', 'http://www.greenfoxacademy.com/');

var second_button = document.querySelector('.this-one');
second_button.disabled = true;

second_button.textContent = "Don't click me!"
