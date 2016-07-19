'use strict';

var addButton = document.querySelector('.add-button');
addButton.addEventListener('click', addItem);

taskContainer.addEventListener('click', function (event) {
  if (event.target.classList.value === 'delete') {
    deleteTask(event, event.target.parentNode.id)
  } else if (event.target.classList.value === 'uncheck') {
    completeTask(event, event.target.parentNode.parentNode.id);
  }
})

function getRequest() {
  readRequest.httpRequest('GET', local, '', function (response) {
    domElements.displayTasks(JSON.parse(response));
  }
);
}

function addItem() {
  readRequest.httpRequest('POST', local, JSON.stringify({text: inputField.value}), function (response) {
    domElements.displayOneItem(JSON.parse(response));
  })
};

function completeTask(event, newLi) {
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  readRequest.httpRequest('PUT', local + serverId, JSON.stringify({completed: true}), function (response) {
    domElements.checkTask(event, id);
  }
)}

function deleteTask(event) {
  var id = event.target.parentNode.id;
  var serverId = id.slice(1,10);
  readRequest.httpRequest('DELETE', local + serverId, JSON.stringify({destroyed: true}), function (response) {
    document.getElementById(id).remove();
  })
}

getRequest();
