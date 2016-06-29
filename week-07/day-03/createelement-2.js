// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var asteroidList = document.querySelector('ul.asteroids');

var king = document.querySelector('li');
asteroidList.removeChild(king);

var fox = document.createElement('li');
fox.textContent = 'The Fox';
var fox2 = document.createElement('li');
fox2.textContent = 'The Fox';
var fox3 = document.createElement('li');
fox3.textContent = 'The Fox';

asteroidList.appendChild(fox);
asteroidList.appendChild(fox2);
asteroidList.appendChild(fox3);
