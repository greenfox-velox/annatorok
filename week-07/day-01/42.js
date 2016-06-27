'use strict';

// create a function that returns it's input factorial

var factor = 1;

function factorial(input) {
  for (var i = 1; i < input+1; i++) {
    factor *= i;
  }
  return factor;
}

console.log(factorial(5));
