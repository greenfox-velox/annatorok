'use strict';
// Create a simple web app, that can yodanize a sentence
// Have an input field and a button.
// On hitting the button, send a request to the Yoda API, with the content of the input field
// Display the response
// The Yoda API: https://market.mashape.com/ismaelc/yoda-speak

var access_token = 'dqVURzgwiBmshONNKdnwW755zvKyp1rXrXRjsn15oW57whOvzF';

var submitButton = document.querySelector('#submit');
var inputField = document.querySelector('input');
var displayResult = document.querySelector('p');

function getYodanated() {
  notLoadedYet();
  var xhr = new XMLHttpRequest();
  var text = inputField.value;
  var responseUrl = 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(text);
  xhr.open('GET', responseUrl);
  xhr.setRequestHeader('X-Mashape-Key', access_token);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      loaded();
      displayResult.textContent = xhr.response;
    }
  };
  xhr.send();
}

submitButton.addEventListener('click', function () {
  getYodanated();
})

function notLoadedYet() {
  document.querySelector('.loading').style.display = "block";
}

function loaded() {
  document.querySelector('.loading').style.display = "none";
}
