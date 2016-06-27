'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minimal_element(input) {
  var minimal = input[0];
  for (var i = 0; i < input.length; i++) {
    if (input[i] < minimal) {
      minimal = input[i];
    }
  }
  return minimal
}

console.log(minimal_element(numbers));
