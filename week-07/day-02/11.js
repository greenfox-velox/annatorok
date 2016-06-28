'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element from the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.elements = [];
  this.elementsNumber = 0;
  this.size = function () {
      return this.elementsNumber;
  },
  this.push = function (item) {
    this.elements[this.elementsNumber] = item;
    this.elementsNumber++;
  },
  this.pop = function () {
    var lastElement = this.elements[this.elements.length-1];
    this.elements.length--;
    return lastElement;
    }
  };

var stack = new Stack();

stack.push(2);
stack.push(6);
stack.push(9);

console.log(stack.elements);
console.log(stack.size());
console.log(stack.pop());
console.log(stack.elements);
console.log(stack.size());
