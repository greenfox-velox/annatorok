'use strict';

// create a page: it should have a button that fires a request to the calendar api described here if it responses, it should wirte the current work day and how many celebrations are on that day

var button = document.querySelector('button');
button.addEventListener('click', clickMe)

function clickMe () {
  var xhr = new XMLHttpRequest();
  xhr.onload = function () {
    console.log(JSON.parse(xhr.response).weekday);
    console.log(JSON.parse(xhr.response).celebrations.length);
  };
  xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/6')
  xhr.send();
}
