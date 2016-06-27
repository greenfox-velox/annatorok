'use strict';

// create a function that returns it's input factorial

var factor = 1;

function factorial(input) {
  for (var i = 0; i < input.length+1; i++) {
    factor *= i;
  }
  return factor;
}

console.log(factorial(5));
