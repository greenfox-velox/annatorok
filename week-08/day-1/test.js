'use strict';

//  test the 1st exercise of day 1
var file = require('./1');
var tape = require('tape');

tape(function (t) {
  t.deepEqual(file.countLetters('apple'), { a: 1, p: 2, l: 1, e: 1} );
  t.end();
});

//  test the 2nd exercise of day 1

var file2 = require('./2');
var tape = require('tape');

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];


tape(function (t) {
  t.equal(file2.countBooks(students),4);
  t.end();
})

//  test the 3rd exercise of day 1

var file3 = require('./3');
var tape = require('tape');

tape(function (t) {
  var rectangle1 = new file3.Rectangle(3,4);
  t.deepEqual(rectangle1.getArea(), 12);
  t.deepEqual(rectangle1.getCircumference(), 14);
  t.end();
});

//  test the 4th exercise of day 1
