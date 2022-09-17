const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => console.log(`listening at ${port}`));

/* provides access to all files within the specified folder */
app.use(express.static('Public'));
app.use(express.json({limit: '1mb'}));

/* gives paths to web pages within the site */
app.get('/', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/jokes.html');
});

app.get('/add_joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/add_joke.html');
});

app.get('/hear_joke.html', (req, res) => {
    res.sendFile(__dirname + '/Public/HTML/hear_joke.html');
});

/* manage database */
const database = [];

/* add joke to database */
app.post('/add', (req, res) => {
    const data = req.body;

    console.log(data);
    console.log(database);

    const firstn = data.fn;
    const lastn = data.ln;
    const orig = data.orig;
    const restrict = data.restrict;
    const joke = data.joke;

    console.log(`first name value: ${firstn}`);
    console.log(`last name value: ${lastn}`);
    console.log(`original value: ${orig}`);
    console.log(`restrict value: ${restrict}`);
    console.log(`joke value: ${joke}`);
});

/* hear joke from database */
