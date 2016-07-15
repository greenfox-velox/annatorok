var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

var instaUrl = 'https://api.instagram.com/v1/media/search?lat=';

app.use(bodyParser.json());

app.use(express.static('insta'));

// app.get(instaUrl + latitude + '&lng=' + longitude + '&access_token=' + access_token, function(req, res) {
//   res.send(result);
// });


app.listen(3001);
