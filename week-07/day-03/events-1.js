'use strict';

  // Turn the party on and off by clicking the button.

var button = document.querySelector('button');
var div = document.querySelector('div')


 function partyOn () {
   div.classList.add('party');
 }
 button.addEventListener('click', partyOn);
