'use strict';

// 1. Alert the content of the header.
var h1 = document.querySelector('h1');
alert(h1);

// 2. Write the content of the first paragraph to the console.

var paragraph = document.querySelector('p');
console.log(paragraph);

// 3. Alert the content of the second paragraph.
var second_paragraph = document.querySelector('.other');
alert(second_paragraph);

// 4. Replace the heading's content with 'New content'.
var new_heading = document.querySelector('h1');
console.log(h1.textContent);
h1.textContent = 'New content';

// 5. Replace the last paragraph's content with the first paragraph's content.
var last_p_content = document.querySelector('.result');
last_p_content.textContent = paragraph.textContent;
