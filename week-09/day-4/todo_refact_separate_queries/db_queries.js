'use strict';

var mysql = require('mysql');

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

function getTodos(callback) {
  con.query('SELECT * FROM todoList', function (err, result) {
    if (err) {
      console.log(err);
      return;
    }
    callback(result);
  });
}

function getOneTodoItem(id, callback) {
  con.query('SELECT * FROM todoList WHERE id = ' + id, function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
  callback(result[0]);
  });
}

function addOneItem(text, callback) {
  con.query('INSERT INTO todoList SET text = ?', text, function (err, result) {
    if (err) {
            console.log(err);
      return;
    }
    callback({ id: result.insertId, text: text });
    });
}

function checkItem(id, completed, callback) {
  con.query('UPDATE todoList SET completed = 1 WHERE id = ' + id, function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
  callback({id: id, completed: true });
  console.log(completed)
  });
}

function deleteItem(id, callback) {
  con.query('DELETE from todoList WHERE id = ' + id, function (err, result) {
       if (err) {
            console.log(err);
            return;
  }
  callback({destroyed: true});
  });
}

module.exports = {
  getTodos: getTodos,
  getOneTodoItem: getOneTodoItem,
  addOneItem: addOneItem,
  checkItem: checkItem,
  deleteItem: deleteItem }
