'use strict';

// fill every paragraph with the last one's content.

var paragraphs = document.querySelectorAll('p');
var last_paragraph = document.querySelector('.dog');

for (var i = 0; i < paragraphs.length; i++) {
  paragraphs[i].textContent = last_paragraph.textContent;
}

// paragraphs.forEach(function (e) {
//   e.paragraphs.textContent = last_paragraph.textContent;
// })
