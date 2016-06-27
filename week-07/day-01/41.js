'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function add_numbers(input) {
  var total = 0;
  for (var i = 0; i < input.length; i++) {
    total += input[i];
  }
  return total;
}

console.log(add_numbers(numbers));
