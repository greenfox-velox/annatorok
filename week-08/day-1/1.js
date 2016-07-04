'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLetters(string) {
  var letters = {};
  var letterList = string.split('');
  letterList.forEach(function (e) {
    letters[e] = letters[e] + 1 || 1;
  })
  return letters;
};
console.log(countLetters('alma'));


function countLetters2(string) {
  return string.split('').reduce(function (string,letter) {
   string[letter] = string[letter] + 1 || 1;
  }, {});
}

console.log(countLetters2('alma'));

module.exports.countLetters = countLetters;

// function count_letters(string) {
//  var arr1 = string.split('');
//  var result = {};
//
//  for (var i = 0; i < arr1.length; i++) {
//    var item = arr1[i];
//    result[item] = (result[item] + 1) || 1;
//  }
//  return result;
// }
//
// console.log(count_letters('alma'));
