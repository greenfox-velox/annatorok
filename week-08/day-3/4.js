'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

var fs = require('fs');

function concatContent(fileOne, fileTwo, cb) {
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

// function concatContent(fileOne, fileTwo, cb) {
//   fs.readFile(fileOne, function (err, content1) {
//     if (err) {
//       return cb(err);
//     }
//     fs.readFile(fileTwo, function (err, content2) {
//       if (err) {
//         return cb(err);
//       }
//     var textConcat = String(content1) + String(content2);
//     cb(null, textConcat);
//   })
//   })
// }
//
// concatContent('text.txt', 'alma.txt', function (err, concat) {
//   console.log(err, concat);
// })
