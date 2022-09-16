const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => console.log(`listening at ${port}`));

app.use(express.static('Public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/jokes.html');
});

app.get('/add_joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/add_joke.html');
});

app.get('/hear_joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/hear_joke.html');
});

