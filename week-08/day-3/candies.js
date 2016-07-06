'use strict';
// Candy game

// gather 10.000 candies! clicking the ‘Create candies’ button gives you 1 candy. you can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button. 10 lollipops generate 1 candy per second.

var numberOfCandies = 0;
var numberOfLollipops = 0;
var candiesPerSecond = 0;

var candyButton = document.querySelector('.create-candy');
var lollipopButton = document.querySelector('.buy-lollipop');

var candies = document.querySelector('.number-of-candies');
var lollipops = document.querySelector('.number-of-lollipops');
var candiesPerSecond = document.querySelector('.candies-per-second');


function displayCandies() {
  candies.textContent = numberOfCandies;
}

function displayLollipops() {
  lollipops.textContent = numberOfLollipops;
}

function candiesCounter() {
  numberOfCandies++;
  displayCandies();
  checkLollipopButton();
}

function lollipopCounter() {
  displayLollipops();
  checkLollipopButton();
}

function checkLollipopButton() {
  if (numberOfCandies >= 10) {
    lollipopButton.removeAttribute('disabled');
  } else {
    lollipopButton.setAttribute('disabled', '');
  }
}

function buyLollipop() {
  if (numberOfCandies >= 10) {
    numberOfCandies -= 10;
    numberOfLollipops++;
    lollipopCounter();
    displayCandies();
    displayLollipops();
  }
}

function generateOneCandyPerSecond(){
  if (numberOfCandies >= 10) {
    numberOfCandies += Math.floor(numberOfLollipops/10);
    displayCandies()
    checkLollipopButton();
  }
  if (numberOfCandies === 1000) {
    alert('You reached 1000 lollipops, YAY!');
  }
}

setInterval(generateOneCandyPerSecond, 1000);

candyButton.addEventListener('click', candiesCounter);
lollipopButton.addEventListener('click', buyLollipop);
