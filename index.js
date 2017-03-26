var express = require('express')
var app = express();
var http = require('http').Server(app);
var path = require('path');
// Prepend the path to public folder to static urls
app.use(express.static(path.join(__dirname, 'public')));
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})