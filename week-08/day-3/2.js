'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

var fs = require('fs');


function countLetters(filename, letter, cb) {
  fs.readFile(filename, function (err, content) {
    if (err) {
      return cb(err);
    }
    var text = String(content).split('');
    var result = 0;
    text.forEach(function (e) {
      if (e === letter) {
        result++;
      }
    })
    cb(null, result);
  })
}


countLetters('text.txt', 'a', function (err, count) {
  console.log(err, count);
});
