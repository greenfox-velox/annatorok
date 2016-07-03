'use strict';

// Remove the king from the list.

var asteroidList = document.querySelector('ul.asteroids');

var king = document.querySelector('li');
asteroidList.removeChild(king);

// Fill the list based on the following list of objects:

var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

for (var i = 0; i < planetData.length; i++) {
  var create_listItems = document.createElement('li');
  if (planetData[i]['asteroid']) {
    asteroidList.appendChild(create_listItems);
    create_listItems.textContent = planetData[i]['content'];
    create_listItems.classList.add(planetData[i]['category'])
  }
}

// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.
