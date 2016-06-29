'use strict';

// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

var asteroidList = document.querySelector('ul.asteroids');


var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';

var newAsteroid2 = document.createElement('li');
newAsteroid2.textContent = 'The Lamplighter ';

asteroidList.appendChild(newAsteroid);
asteroidList.appendChild(newAsteroid2);

var container = document.querySelector('.container');

var heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM';

container.appendChild(heading);

var img = document.createElement('img');
img.setAttribute('src', 'https://static.wixstatic.com/media/f4461b_83457ca5dd844c71a760d36e6583d0ff.png/v1/fill/w_168,h_168,al_c,usm_0.66_1.00_0.01/f4461b_83457ca5dd844c71a760d36e6583d0ff.png')

container.appendChild(img);
