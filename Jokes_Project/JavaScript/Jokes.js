const port = 3000;
var path = require('path');
var fs = require('fs');
var http = require('http');
const express = require('express');
const app = express();

app.listen(port, () => console.log('listening at 3000'));
app.use(express.static(__dirname + '..'));

app.use(express.json());

/* adding jokes */
app.post('/', (request, response) => {
    console.log('Joke Added!!');
});

/* hearing jokes */
app.get('/', (request, response) => {
    console.log('Jokes Requested!!');
})