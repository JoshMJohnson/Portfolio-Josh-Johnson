const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => console.log(`listening at ${port}`));

app.use(express.static('Public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/Jokes.html');
});

app.get('/Add_Joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/Add_Joke.html');
});

app.get('/Hear_Joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/Hear_Joke.html');
});

