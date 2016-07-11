'use strict';
// Todo app with Express
//
// Routes
//
// All routes expects and returns JSON documents.
//
// GET /todos
//
// List all todo items.
//

var todoList = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
]


var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var id = 3;
app.use(bodyParser.json());

app.get('/todos', function(req, res) {
  res.send(todoList);
});

function getOneTodo(id) {
  for (var i = 0; i < todoList.length; i++) {
    if (parseInt(todoList[i].id) === parseInt(id)) {
      return todoList[i];
    }
  }
}

app.get('/todos/:id', function (req, res) {
  res.send(getOneTodo(req.params.id));
});

function newTodoItem(newText) {
  id++;
  var newTodo = {'completed': false, 'id': id, 'text': newText};
  todoList.push(newTodo);
  return newTodo
}

app.post('/todos', urlencodedParser, function(req, res) {
  res.send(newTodoItem(req.body.text));
})

function modifyTodoItem(id, newText) {
  for (var i = 0; i < todoList.length; i++) {
    if (parseInt(todoList[i].id) === parseInt(id)) {
      todoList[i].completed = true;
      todoList[i].text = newText;
      return todoList[i];
    }
  }
}
  // return todoList.filter(function (e) {
  //   if (parseInt(e.id) === parseInt(id)) {
  //     e.completed = true;
  //     e.text = newText;
  //   } nem jo, mert listat ad vissza objektum helyett, ezert [0] elemet kell venni

app.put('/todos/:id', function(req, res) {
  res.send(modifyTodoItem(req.params.id, req.body.text));
})

function deleteTodoItem(newTodo) {
  for (var i = 0; i < todoList.length; i++) {
    if (parseInt(todoList[i].id) === parseInt(id)) {
      todoList[i].destroyed = true;
      return todoList.splice(i, 1)[0];
    }
  }
}

app.delete('/todos/:id', urlencodedParser, function(req, res) {
  if (err) {
    res.status(404);
  } else {
    res.send(deleteTodoItem(req.params.id));
  }
});

app.listen(3000);
