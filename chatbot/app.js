var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var routes = require('./routes/index');
var app = express();
 
app.use(logger('dev'));

var path = __dirname + '/src/app';
var index_file = path + '/index.html'
 
app.set('port', (process.env.PORT || 5000));

app.use(express.static(path));
app.use(fallback(path + 'index.html', { path }));


app.all('*', (req, res) => {
  res.status(200).sendFile(index_file);
});
 
module.exports = app;