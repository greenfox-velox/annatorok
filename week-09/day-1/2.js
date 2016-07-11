'use strict';
// Excercise with Express
//
// Create a webserver that can receive any request to any path. It should respond the path name, the request methos and the current time.

var express = require('express');
var app = express();

app.get('*', function(req, res) {
  var date = new Date();
  res.send('Method is: ' + req.method + '\nURL path is: ' + req.url + '\nDate is: ' + date);
});

app.listen(3000);
