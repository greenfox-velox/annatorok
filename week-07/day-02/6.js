'use strict';

// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var i = 0;

function boolean(string, letter) {
    return string.indexOf(letter) !== -1;
}

// 2. solution
// function isLetterInString(string, letter) {
//  return string.split('').some(function (e) {
//    return (e === letter);
//  });
// }

//3. solution
// function isLetterInString(string, letter) {
//  var letters = string.split('');
//  return letters.some(function (e) {
//    return (e === letter);
//  });
// }


console.log(boolean('alma', 'a'));
