'use strict';

var af = [4, 5, 6, 7];
var i = 0;
// print all the elements of af


while (af.length > i) {
  console.log(af[i]);
  i += 1;
}

for (i = 0; af.length > i; i++) {
  console.log(af[i]);
}
