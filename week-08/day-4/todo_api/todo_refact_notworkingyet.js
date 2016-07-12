'use strict';

var local = 'http://127.0.0.1:3000/todos';
var todoUrl = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var addButton = document.querySelector('.add-button');
var inputField = document.querySelector('input');
var taskContainer = document.querySelector('ul');

addButton.addEventListener('click', addItem);

// var response = JSON.parse(xhr.response);

function httpRequest(method, url, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(data);
  if (xhr.readyState === xhr.DONE) {
    callback(xhr.response);
  }
};

function getRequest() {
  httpRequest('GET', todoUrl, '', function (response) {
    displayTasks(JSON.parse(response));
  }
);
}

function addItem(newLiText) {
  httpRequest('POST', todoUrl, JSON.stringify({text: newLiText}), function (response) {
    displayOneItem(response);
  })
};

function displayOneItem(e) {
  var newLi = document.createElement('li');
  newLi.textContent = e.text;
  newLi.setAttribute('id', 'l' + e.id)
  taskContainer.appendChild(newLi);
  createDeleteButton(newLi, e);
  createCheckButton(newLi, e);
  inputField.value = '';
}

function displayTasks(response) {
  // var taskList = JSON.parse(xhr.response);
  response.forEach(function (e) {
    displayOneItem(e);
  })
}

function completeTask(event, newLi) {
  httpRequest('PUT', todoUrl + '/' + serverId, '', JSON.stringify({text: newLiText, completed: 'true'}), function (response) {
    var id = event.target.parentNode.id;
    var serverId = id.slice(1,10);
    var newLiText =  event.target.parentNode.textContent;
    checkTask(event, id);
  }
)}

function deleteTask(event) {
  httpRequest('DELETE', todoUrl + '/' + serverId, '', function (response) {
    var id = event.target.parentNode.id;
    var serverId = id.slice(1,10);
    document.getElementById(id).remove();
  })
}

function createDeleteButton(newLi, e) {
  var deleteButton = document.createElement('button');
  deleteButton.classList.add('delete');
  deleteButton.setAttribute('id', 'd' + e.id)
  newLi.appendChild(deleteButton);
  deleteButton.addEventListener('click', function(event) {  // mi ez???????
    deleteTask(event);
  });
}

// function removeTaskFromDisplay() {
//   var allLi = document.querySelectorAll('li');
//   for (var i = 0; i < allLi.length-1; i++) {
//     if (allLi[i].id === event.target.id) {
//       taskContainer.removeChild(allLi[i]);
//     }
//   }
// }

function createCheckButton(newLi, e) {
  var checkButton = document.createElement('button');
  if (e.completed) {
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

function checkTask(event, id) {
  // console.log(buttons);
  var button = document.querySelector('#' + event.target.id);
  button.classList.toggle('check');
  button.classList.toggle('uncheck');
}

getRequest();
