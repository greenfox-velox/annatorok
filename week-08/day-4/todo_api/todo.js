'use strict';

var local = 'http://127.0.0.1:3000/todos';
var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var addButton = document.querySelector('.add-button');
var inputField = document.querySelector('input');
var taskContainer = document.querySelector('ul');

function getRequest() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', local);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      displayTasks(xhr);
    }
  };
  xhr.send();
}

function displayTasks(xhr) {
  var taskList = JSON.parse(xhr.response);
  taskList.forEach(function (e) {
    displayOneItem(e);
  })
}

function displayOneItem(e) {
  var newTask = document.createElement('li');
  newTask.textContent = e.text;
  newTask.setAttribute('id', 'l' + e.id)
  taskContainer.appendChild(newTask);
  createDeleteButton(newTask, e);
  createCheckButton(newTask, e);
  inputField.value = '';
}

function addItem() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  var newTaskText = inputField.value;
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      var response = JSON.parse(xhr.response);
      displayOneItem(response);
    }
  }
  xhr.send(JSON.stringify({text: newTaskText}));
}

function createDeleteButton(newTask, e) {
  var deleteButton = document.createElement('button');
  deleteButton.classList.add('delete');
  deleteButton.setAttribute('id', 'd' + e.id)
  newTask.appendChild(deleteButton);
  deleteButton.addEventListener('click', function(event) {  // mi ez???????
    deleteTask(event);
  });
}

function deleteTask(event) {
  var xhr = new XMLHttpRequest();
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  xhr.open('DELETE', url + '/' + serverId);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      document.getElementById(id).remove();
    }
  };
  xhr.send();
}

// function removeTaskFromDisplay() {
//   var allLi = document.querySelectorAll('li');
//   for (var i = 0; i < allLi.length-1; i++) {
//     if (allLi[i].id === event.target.id) {
//       taskContainer.removeChild(allLi[i]);
//     }
//   }
// }

function createCheckButton(newTask, e) {
  var checkButton = document.createElement('button');
  if (e.completed) {
    checkButton.classList.add('check');
  } else {
    checkButton.classList.add('uncheck');
  }
  checkButton.setAttribute('id', 'c' + e.id)
  newTask.appendChild(checkButton);
  checkButton.addEventListener('click', function(event) {
    completeTask(event, newTask);
  });
}

function completeTask(event, newTask) {
  var xhr = new XMLHttpRequest();
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  var newTaskText =  event.target.parentNode.textContent;
  xhr.open('PUT', url + '/' + serverId);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      checkTask(event, id);
    }
  }
  xhr.send(JSON.stringify({text: newTaskText, completed: 'true'}));
}

function checkTask(event, id) {
  // console.log(buttons);
  var button = document.querySelector('#' + event.target.id);
  button.classList.toggle('check');
  button.classList.toggle('uncheck');
}

addButton.addEventListener('click', addItem);

getRequest();
