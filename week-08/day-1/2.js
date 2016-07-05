'use strict';


var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

// create a function that counts all the books of an array of students
// not every student has a property called books

// function countBooks() {
//   var book = 0;
//   students.forEach(function(e) {
//     book = book + (e.books && e.books.length) || book;
//     // console.log(book);
//     }
//   );
//   return book;
// }
//
// console.log(countBooks(students));

function countBooks() {
  var book = 0;
  students.forEach(function(e) {
    book += e.books && e.books.length || 0;
    // console.log(book);
  }
  );
  return book;
}

function countBooksReduce(input) {
  var bookz = input.reduce(function (book, e) {
    return book += e.books && e.books.length || 0;
  }, 0);
  return bookz;
}

console.log(countBooks(students));
console.log(countBooksReduce(students));

module.exports.countBooks = countBooks;
