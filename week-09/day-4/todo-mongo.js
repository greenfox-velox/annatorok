'use strict';

// not working yet!!

var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var id = 0;

app.use(bodyParser.json());
app.use(express.static('../../week-08/day-4/todo_api'));

var url = 'mongodb://localhost:27017/todos';

MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

    var collection = db.collection('todos');

    app.get('/todos', function(req, res) {
    collection.find({} ,{'id': 1, 'text': 1, '_id': 0 ,'completed':1,'destroyed': true}).toArray(function (err, result) {
     if (err) {
       console.log(err);
     }
       res.send(result);
       return (id = result.length)
     });
     });

     app.get('/todos/:id', function(req, res) {
     var req_id = parseInt(req.params.id);
     collection.find({'id': req_id}, {'id': 1, 'text': 1, '_id': 0, 'destroyed': 1}), (function (err, result) {
      if (err) {
        console.log(err);
      }
        res.send(result);
      });
      });

      app.post('/todos', function(req, res) {
      collection.insert({'text': req.body.text, 'id':id ,'completed':false}), (function (err, result) {
       if (err) {
         console.log(err);
       }
        res.send(JSON.stringify({ 'id': parseInt(id) ,'text': req.body.text,'completed':false}));
        return (id++);
       });
       });

       app.put('/todos/:id', function(req, res){
       collection.update({'id': parseInt(req.params.id)}, {$set:{'completed':true}}, function(err, result){
       if (err) {
         console.log(err);
       }
       res.send({'id': parseInt(req.params.id), 'completed':true})
         })
       });

     app.delete('/todos/:id', function(req, res){
       collection.update({'id': parseInt(req.params.id)}, {$set:{'destroyed':true}}, function(err, result){
       if (err) {
         console.log(err);
       }
       res.send({'id': parseInt(req.params.id),'destroyed': true})
         })
       });

    app.listen(3000);
     }
  });
