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
  return this.balance -= this.price;
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
  this.income = 0;
}
//
// Methods:
// carEnter(car)
//  - It should add a car to the garage and add its stored startTime
//

CarPark.prototype.carEnter = function(car) {
  this.garage.push(car);
  car.enter(new Date().getTime());
}
// carLeave(id)
//  - It should remove the car with the given id and it should charge from its balance
//

CarPark.prototype.carLeave = function(id) {
  this.garage.forEach(funciton (e) {
    if (car.id === id) {

    }
  })
  // splice(carId)
}

// elapseTime(hours)
//  - It should increment the time with the hours
//

CarPark.prototype.elapseTime = function(hours) {

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

// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours

// CarPark.prototype.getParkingCarsSince = function(hours) {
//
// }
