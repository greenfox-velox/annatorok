/////////////////////////////////////
// function foo(data)
// {
    // do stuff with JSON
// }
//
// var script = document.createElement('script');
// script.setAttribute('src', 'http://localhost.com:3001/jsonp?callback=foo');
//
// document.head.appendChild(script);

///////////////////////////////////

var googleUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address=';
// var instaUrl = 'https://api.instagram.com/v1/media/search?lat=';
var panoUrl = 'https://crossorigin.me/http://www.panoramio.com/map/get_panoramas.php?set=public&from=0&to=20&minx=-180&miny=-90&maxx=180&maxy=90&size=medium&mapfilter=false'
var access_token = '1313861570.62797d0.8558a95fbcda4b91872abe6e757358be';
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
      h3.textContent = 'The latitude is: ' + latitude +  ', and the longitude is: ' + longitude;
      result.appendChild(h3);
      // getInstaRequest(latitude, longitude);
      getPanoramioRequest(latitude, longitude);
    }
  };
  xhr.send();
}

function getPanoramioRequest(latitude, longitude) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', panoUrl);
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      var response = JSON.parse(xhr.response);
      console.log('macska');
      console.log(response);
      for (var i = 0; i < response.photos.length; i++) {
        console.log(response.photos);
        var images = document.createElement('img');
        var container = document.createElement('p');
        var imagesContainer = document.querySelector('p');
        images[i].setAttribute('src', photos[0].photo_file_url);
        imagesContainer.appendChild(images[i]);
        result.appendChild(imagesContainer);
      }
    }
  };
  xhr.send();
}

// function getInstaRequest(latitude, longitude) {
//   var xhr = new XMLHttpRequest();
//   xhr.open('GET', instaUrl + latitude + '&lng=' + longitude + '&access_token=' + access_token);
//   xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
//   xhr.setRequestHeader('Content-Type', 'application/json');
//   xhr.onload = function() {
//     if (xhr.readyState === xhr.DONE) {
//       // response.forEach(function (e) {
//       //   document.createElement('img');
//       //   img.setAttribute('src', response[e],  'data[0].images.low_resolution')
//       // result.appendChild(p);
//     }
//   };
//   xhr.send();
// }

searchButton.addEventListener('click', getGoogleRequest);
