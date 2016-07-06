'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');


function countWords(filename, cb) {
  fs.readFile(filename, function (err, content) {
    if (err) {
      return cb(err);
    }
    cb(null, String(content).split(/\s/g).length-1);
    // var count = String(content).split('/\s/').length-1;
    // cb(null, count);
  });
}

countWords('text.txt', function (err, count) {
  console.log(err, count);
});

// own wrong version
// function countWords(filename) {
//   fs.readFile(filename, function (err, count) {
//     var count = String(count).split(' ').length;
//   });
// }
//
// countWords('text.txt', function (err, count) {
//   console.log(err, count);
// });
