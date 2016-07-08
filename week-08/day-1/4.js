'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)
//
// every car should have an id property (a number), that is
// unique for all the cars, starting from 0
//
// Methods:
// enter(enterDate)
//  - it should store the date of entering
//
// getEnterDate()
//  - it should return the date of the last entering
//
// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)
//
// getStats()
//  - it should give back a string like:
//    "Type: volvo, Color: red, Balance: 500"

var carId = 0;

function Car(type, color, balance) {
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.dateOfEntering = 0;
  this.id = carId++;
}

Car.prototype.enter = function(enterDate) {
  this.dateOfEntering = enterDate;
}

Car.prototype.getEnterDate = function() {
  return this.dateOfEntering;
}

Car.prototype.leave = function(price) {
  this.balance -= price;
}

Car.prototype.getStats = function() {
  return 'Type: ' + this.type + ', Color: ' + this.color + ', Balance: ' + this.balance;
}

var volvo = new Car('Volvo', 'red', '500');
console.log(volvo.getStats());

//
// Create a CarPark constructor
// it should take 2 parameters
//  - income: the initial credits as a number (eg: 4000)
//  - startTime: the current date
//  The parking fee: 40 per hours (only every whole hour)

function CarPark(income, startTime) {
  this.income = income;
  this.startTime = startTime;
  this.garage = [];
  this.parkingFeePerHour = 40;
}
//
// Methods:
// carEnter(car)
//  - It should add a car to the garage and add its stored startTime
//

CarPark.prototype.carEnter = function(car) {
  this.garage.push(car);
  car.enter(this.startTime);
}
// carLeave(id)
//  - It should remove the car with the given id and it should charge from its balance
//

CarPark.prototype.carLeave = function(id) {
  this.garage.forEach(function (e, i) {
    if (e.id === id) {
      var fee = this.parkingFeePerHour * (this.startTime - e.getEnterDate()) / 3600000;
      e.leave(fee);
      this.income += fee;
    }
  });
  this.garage.splice(i, 1);
}

// elapseTime(hours)
//  - It should increment the time with the hours
//

CarPark.prototype.elapseTime = function(hours) {
  this.startTime += hours * 3600000
}

// Optional Methods:
//
// getStats()
//  - It should return a string like:
//    "Cars: 4, Time: 1234423453, Income: 1400"
//

CarPark.prototype.getStats = function() {
  return 'Cars: ' + this.garage.length + ', Time: ' + this.startTime + ', Income: ' + this.income;
}

var car1 = new Car('volvo', 'red', 500);
var car2 = new Car('mazda', 'blue', 600);
var car3 = new Car('lada', 'yellow', 300);

var garage = new CarPark(100, new Date().getTime());

garage.carEnter(car1);
garage.carEnter(car2);
garage.carEnter(car3);
console.log(car1.id);
console.log(car2.id);
console.log(car3.id);
console.log(car2.balance);
console.log(garage.income);
console.log(garage.garage);

garage.elapseTime(5);

garage.carLeave(2);

console.log(car2.balance);
console.log(garage.income);
console.log(garage.garage);

console.log(garage.getStats());


// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours

// CarPark.prototype.getParkingCarsSince = function(hours) {
//   return this.garage[i]
// }
