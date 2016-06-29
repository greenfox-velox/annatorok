// fill output1 with the first paragraph's content, text only.
// fill output2 with the first paragraph's content keeping the cat strong.

'use strict';

var output1 = document.querySelector('.output1');
var first_paragraph = document.querySelector('p:first-child');
var output2 = document.querySelector('.output2');

output1.textContent = first_paragraph.textContent;
output2.innerHTML = first_paragraph.innerHTML;
