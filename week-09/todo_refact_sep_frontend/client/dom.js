'use strict';

var inputField = document.querySelector('input');
var taskContainer = document.querySelector('ul');

var domElements = (function () {
  function displayOneItem(e) {
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

  function checkTask(event, id) {
    var button = document.querySelector('#' + event.target.id);
    button.classList.toggle('check');
    button.classList.toggle('uncheck');
  }

  function createDeleteButton(newLi, e) {
    var deleteButton = document.createElement('button');
    deleteButton.classList.add('delete');
    deleteButton.setAttribute('id', 'd' + e.id)
    newLi.appendChild(deleteButton);
  }

  function createCheckButton(newLi, e) {
    var checkButton = document.createElement('button');
    if (e.completed === 1) {
      checkButton.classList.add('check');
    } else {
      checkButton.classList.add('uncheck');
    }
    checkButton.setAttribute('id', 'c' + e.id)
    newLi.appendChild(checkButton);
  }
  return {
    displayOneItem: displayOneItem,
    displayTasks: displayTasks,
    checkTask: checkTask,
    createDeleteButton: createDeleteButton,
    createCheckButton: createCheckButton
  }
})();
