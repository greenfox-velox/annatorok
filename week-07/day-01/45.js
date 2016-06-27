'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortest_string(input) {
  var shortest = input[0];
  for (var i = 0; i < input.length; i++) {
    if ((input[i]).length < shortest.length) {
      shortest = input[i]
    }
  }
  return shortest
}

console.log(shortest_string(names));
