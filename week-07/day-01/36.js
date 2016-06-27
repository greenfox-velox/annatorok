'use strict';

var ah = [3, 4, 5, 6, 7];
var total = 0
var i = 0
// print the sum of all numbers in ah

while (i < ah.length) {
  total += ah[i];
  i += 1;
}

console.log(total);

for (i = 0; i < ah.length; i++) {
  total += ah[i];
}

console.log(total);
