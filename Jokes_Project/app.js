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
const sqlite3 = require('sqlite3').verbose();
const database = 'jokes.db';

/* connect to database */
const db = new sqlite3.Database(database, sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        return console.error(err.message);
    }

    console.log('Connection to database was successful');
})

/* create database table to hold jokes */ /*
db.run (
    `CREATE TABLE jokes (
        id                  INTEGER     PRIMARY KEY
                                        AUTOINCREMENT, 
        dateContributed     DATETIME    TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        fullName            TEXT        NOT NULL, 
        originalJoke        TEXT        NOT NULL, 
        ageRestricted       BOOLEAN     NOT NULL, 
        joke                STRING      NOT NULL
                                        UNIQUE
    );`
); */

/* insert joke data into the database */
app.post('/add', (req, res) => {
    const data = req.body;
    const full_name = `${data.fn} ${data.ln}`;
    const orig = data.orig;
    const restrict = data.restrict;
    const joke = data.joke;

    const sql_insert = `INSERT INTO jokes (fullName, originalJoke, ageRestricted, joke)
                            VALUES (?, ?, ?, ?)`;

    db.run(
        sql_insert, [full_name, orig, restrict, joke], (err) => {
            if (err) {
                return console.error(err.message);
            }

            console.log("Joke was added to the database!!");
    });
});

/* hear joke from database */







