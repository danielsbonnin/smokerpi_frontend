var express = require('express');
var app = express();
var http = require('http').Server(app);
var path = require('path');
var util = require('util');
var spawn = require('child_process').spawn;
var proc = spawn("python", [path.join(__dirname, "tempHistory.py")]);
util.log('readingin');

var fs = require('fs');

var io = require('socket.io')(http);

proc.stdout.on('data', function(chunk){
    var data = chunk.toString('utf8');
    io.emit('tempData', JSON.parse(data));
    util.log(data);
});

// Prepend the path to public folder to static urls
app.use(express.static(path.join(__dirname, 'public')));
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});
io.on('connection', function(socket){
    console.log('a user connected');
    io.emit('newTemp', {temp: 1});
});

http.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})

