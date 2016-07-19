'use strict';

var databaseQueries = require('./db_queries');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('client'));


app.get('/todos', function(req, res) {
  databaseQueries.getTodos(function (result) {
    res.send(result);
  });
});

app.get('/todos/:id', function (req, res) {
  databaseQueries.getOneTodoItem(req.params.id, function (result) {
    res.send(result);
  });
});

app.post('/todos', urlencodedParser, function(req, res) {
  databaseQueries.addOneItem(req.body.text, function (result) {
    res.send(result);
  });
});

app.put('/todos/:id', urlencodedParser, function(req, res) {
  databaseQueries.checkItem(req.params.id, req.body.completed, function (result) {
  res.send(result);
});
});

app.delete('/todos/:id', urlencodedParser, function(req, res) {
    databaseQueries.deleteItem(req.params.id, function (result) {
    res.send(result);
});
});

app.listen(3000);
