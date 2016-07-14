'use strict';

var mysql = require("mysql");
var express = require('express');
var app = express();

var con = mysql.createConnection({
  host: "localhost",
  user: 'root',
  password: 'password',
  database: 'bookstore'
});

con.connect();

app.get('/', function(req, res) {
con.query('SELECT book_name FROM book_mast', function (err, result) {
     if (err) {
          console.log(err);
          return;
}
      res.send(result);
})
});

app.get('/', function(req, res) {
con.query('SELECT book_name, book_price, aut_name, cate_descrip, pub_name FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON category.cate_id = book_mast.cate_id JOIN publisher ON publisher.pub_id = book_mast.pub_id', function (err, result) {
     if (err) {
          console.log(err);
          return;
}
    res.send(result);
})
});

app.listen(3000);
