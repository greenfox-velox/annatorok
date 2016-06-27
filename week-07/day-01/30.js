'use strict';

var ac = 8;
var time = 120;
var out = '';
// if ac is dividable by 4
// and time is not more than 200
// set out to 'check'
// if time is more than 200
// set out to 'Time out'
// otherwise set out to 'Run Forest Run!'

if (ac % 4 === 0 && time > 200) {
  out = 'check';
} else if (time > 200) {
  out = 'Time out';
} else {
  out = 'Run Forest Run!';
}

console.log(out);
