'use strict';

// create a function that has 2 paramteres
//  - fileNames: an array of filenames
//  - callback
//
// it should read the files and call the callback with their content concated
// it should have the same order as the filenames
// it should pass the error as a parameter

var fs = require('fs');

var fileNames = ['text.txt', 'alma.txt']

function concatContent(fileOne, cb) {
  fs.readFile(fileOne, function (err, content) {
    if (err) {
      return cb(err);
    }
    var text1 = String(content);
    fs.readFile(fileTwo, function (err, content) {
      if (err) {
        return cb(err);
      }
    var text2 = String(content);
    var textConcat = text1.concat(text2);
    cb(null, textConcat);
  })
  })
}

concatContent('text.txt', 'alma.txt', function (err, concat) {
  console.log(err, concat);
})
