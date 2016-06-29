'use strict';

var output1 = document.querySelector('.output1');
var first_paragraph = document.querySelector('p:first-child');
var output2 = document.querySelector('.output2');

// fill output1 with the first paragraph's content, text only.

output1.textContent = first_paragraph.textContent;

// document.querySelector('.output1').innerHTML = document.querySelector('p').textContent;

// fill output2 with the first paragraph's content keeping the cat strong.

output2.innerHTML = first_paragraph.innerHTML;

// document.querySelector('.output2').innerHTML = document.querySelector('p').innerHTML;
