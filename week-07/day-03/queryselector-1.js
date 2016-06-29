'use strict';

// 1
var king = document.querySelector('#b325');
console.log(king);

// 2
var conceited = document.querySelector('.asteroid.b326');
alert(conceited);

// 3
var businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function (e) {
    console.log(e);
});

// 4
var conceitedKing = document.querySelectorAll('.container div');
conceitedKing.forEach(function (e) {
  alert(conceitedKing);
});

// 5
var noBusiness = document.querySelectorAll('div.asteroid');
noBusiness.forEach(function (e) {
    console.log(e);
});

// 6
var allBizniss = document.querySelector('p');
alert(allBizniss);
