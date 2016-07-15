var googleUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address=';
var instaUrl = 'https://crossorigin.me/https://api.instagram.com/v1/media/search?lat=';
// var panoUrl = 'https://crossorigin.me/http://www.panoramio.com/map/get_panoramas.php?set=public&from=0&to=30&minx=-180&miny=-90&maxx=180&maxy=90&size=medium&mapfilter=false'
var access_token = '';
var inputField = document.querySelector('input');
var searchButton = document.querySelector('.search-button');
var result = document.querySelector('.result');
var h3 = document.createElement('h3');

function getGoogleRequest(event) {
  // we need this because the submit button type is 'submit' and the page refreshes every time so we dont get the request. Now, we prevent this to happen.
  event.preventDefault();
  var xhr = new XMLHttpRequest();
  var location = inputField.value;
  xhr.open('GET', googleUrl + location);
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      var response = JSON.parse(xhr.response);
      var latitude = response.results[0].geometry.location.lat;
      var longitude = response.results[0].geometry.location.lng;
      h3.textContent = 'The latitude is: ' + latitude +  ', and the longitude is: ' + longitude + '.';
      result.innerHTML = '';
      result.appendChild(h3);
      getInstaRequest(latitude, longitude);
      // getPanoramioRequest(latitude, longitude);
    }
  };
  xhr.send();
}

// function getPanoramioRequest(latitude, longitude) {
//   var xhr = new XMLHttpRequest();
//   xhr.open('GET', panoUrl + latitude + longitude);
//   xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
//   xhr.setRequestHeader('Content-Type', 'application/json');
//   xhr.onload = function() {
//     if (xhr.readyState === xhr.DONE) {
//       var response = JSON.parse(xhr.response);
//       for (var i = 0; i < response.photos.length; i++) {
//         // console.log(response.photos[i]);
//           var images = document.createElement('img');
//           var result = document.querySelector('.result');
//           images.setAttribute('src', response.photos[i].photo_file_url);
//           result.appendChild(images);
//       }
//     }
//   };
//   xhr.send();
// }

function getInstaRequest(latitude, longitude) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', instaUrl + latitude + '&lng=' + longitude + '&access_token=' + access_token);
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      var response = JSON.parse(xhr.response);
      for (var i = 0; i < response.data.length; i++) {
          var images = document.createElement('img');
          var result = document.querySelector('.result');
          images.setAttribute('src', response.data[i].images.low_resolution.url);
          result.appendChild(images);
    }
  }
};
  xhr.send();
}

searchButton.addEventListener('click', getGoogleRequest);
