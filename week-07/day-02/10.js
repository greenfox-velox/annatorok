'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  gradeList: [],
  addgrade: function(grade) {
    this.gradeList.push(grade);
    },
  getAverage: function() {
    var total = 0;
    this.gradeList.forEach(function (e) {
      total += e;
    })
    return total / this.gradeList.length;
  }
};

student.addgrade(3);
student.addgrade(5);
student.addgrade(4);
console.log(student.getAverage());
