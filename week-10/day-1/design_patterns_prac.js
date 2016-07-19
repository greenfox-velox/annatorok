'use strict';

// using prototype module

var Dog = function Dog () {
  this.sound = 'woof';
}

Dog.prototype.talk = function () {
  console.log(this.sound)
}

var sniffles = new Dog();
sniffles.talk();


// using module pattern - IIFE

const dog = (function () {
  const sound = 'woof';
  return {
    talk: function () {
      console.log(sound);
    }
  }
})();

dog.talk()


// using revealing module

const dog = (function () {
  const sound = 'woof';
  function publicTalk () {
      console.log(sound);
    }
  return {
    talk: publicTalk
  }
  }
)();

dog.talk()


// without arrow function

const dog = function () {
  const sound = 'woof'
  return {
    talk: function () {
      console.log(sound)
    }
  }
}

const sniffles = dog()
sniffles.talk()


// const dog = () => {
//   const sound = 'woof'
//   return {
//     talk: () => console.log(sound)
//   }
// }
//
// const sniffles = dog()
// sniffles.talk()
