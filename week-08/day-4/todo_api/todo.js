'use strict';

var local = 'http://localhost:3000/todos/';
// var local = 'https://mysterious-dusk-8248.herokuapp.com/todos/';
var addButton = document.querySelector('.add-button');
var inputField = document.querySelector('input');
var taskContainer = document.querySelector('ul');

addButton.addEventListener('click', addItem);

function httpRequest(method, url, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(data);
  xhr.onload = function () {
  if (xhr.readyState === xhr.DONE) {
    callback(xhr.response);
    }
  }
};

function getRequest() {
  httpRequest('GET', local, '', function (response) {
    displayTasks(JSON.parse(response));
  }
);
}

function addItem() {
  httpRequest('POST', local, JSON.stringify({text: inputField.value}), function (response) {
    displayOneItem(JSON.parse(response));
  })
};

function displayOneItem(e) {
  console.log(e.destroyed);
  if (e.destroyed !== true) {
    var newLi = document.createElement('li');
    newLi.textContent = e.text;
    newLi.setAttribute('id', 'l' + e.id)
    taskContainer.appendChild(newLi);
    createDeleteButton(newLi, e);
    createCheckButton(newLi, e);
    inputField.value = '';
  }
}

function displayTasks(response) {
  response.forEach(function (e) {
    displayOneItem(e);
  })
}

function completeTask(event, newLi) {
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  httpRequest('PUT', local + serverId, JSON.stringify({completed: true}), function (response) {
    checkTask(event, id);
  }
)}

function checkTask(event, id) {
  var button = document.querySelector('#' + event.target.id);
  button.classList.toggle('check');
  button.classList.toggle('uncheck');
}

function deleteTask(event) {
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  httpRequest('DELETE', local + serverId, JSON.stringify({destroyed: true}), function (response) {
    document.getElementById(id).remove();
  })
}

function createDeleteButton(newLi, e) {
  var deleteButton = document.createElement('button');
  deleteButton.classList.add('delete');
  deleteButton.setAttribute('id', 'd' + e.id)
  newLi.appendChild(deleteButton);
  deleteButton.addEventListener('click', function(event) {
    deleteTask(event);
  });
}

function createCheckButton(newLi, e) {
  var checkButton = document.createElement('button');
  if (e.completed === true) {
    checkButton.classList.add('check');
  } else {
    checkButton.classList.add('uncheck');
  }
  checkButton.setAttribute('id', 'c' + e.id)
  newLi.appendChild(checkButton);
  checkButton.addEventListener('click', function(event) {
    completeTask(event, newLi);
  });
}

getRequest();
