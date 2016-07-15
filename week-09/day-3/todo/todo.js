'use strict';

var mysql = require('mysql');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var id = 3;
app.use(bodyParser.json());
app.use(express.static('../../../week-08/day-4/todo_api'));

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'Todos'
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.get('/todos', function(req, res) {
  con.query('SELECT * FROM todoList', function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
        res.send(result);
})
});

app.get('/todos/:id', function (req, res) {
  con.query('SELECT * FROM todoList WHERE id = ' + req.params.id, function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
  res.send(result[0]);
  })
});

app.post('/todos', urlencodedParser, function(req, res) {
  con.query("INSERT INTO todoList (text) VALUES ('" + req.body.text + "')", function (err, result) {
    if (err) {
            console.log(err);
      return;
    }
    res.send({ id: result.insertId, text: req.body.text });
  });
});

  app.put('/todos/:id', function(req, res) {
    con.query('UPDATE todoList SET completed = 1 WHERE id =' + req.params.id, function (err, result) {
         if (err) {
              console.log(err);
              return;
    }
    res.send({completed: true });
  })
});

app.delete('/todos/:id', urlencodedParser, function(req, res) {
  con.query('DELETE FROM todoList WHERE id = ' + req.params.id, function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
    res.send({destroyed: true});
})
});

app.listen(3000);
