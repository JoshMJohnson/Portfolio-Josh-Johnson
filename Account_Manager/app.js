/* server side JavaScript for the Account Manager project */
const express = require('express');
const app = express();
const port = 4000;

app.listen(port, () => console.log(`listening at ${port}`));

/* provides access to all files within the specified folder */
app.use(express.static('Public'));
app.use(express.json({limit: '1mb'}));

/* gives paths to web pages within the site */
app.get('/', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/login.html');
});

app.get('/create_account', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/create_account.html');
});

app.get('/logged_in', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/logged_in.html');
});

/* manage database */
const sqlite3 = require('sqlite3').verbose();
const database = 'arrow_fan_club.db';

/* connect to database */
const db = new sqlite3.Database(database, sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        return console.error(err.message);
    }

    console.log('Connection to database was successful');
});

/* create database table to hold fan club members */ /*
db.run (
    `CREATE TABLE members (
        email       STRING       PRIMARY KEY
                                 UNIQUE
                                 NOT NULL,
        name        STRING       NOT NULL,
        dob         DATE,
        phoneNumber VARCHAR (12),
        password    STRING,
        avatar      INTEGER      NOT NULL,
        status      STRING       DEFAULT member
    );`
); */

/* retrieves the fan club members from the database */
app.get('/members', (request, response) => {
    const sql = `SELECT * FROM members`;
    const sendBack = [];

    db.all(
        sql, [], (err, rows) => {
            if (err) {
                return console.error(err.message);
            }
            
            rows.forEach((row) => {
                sendBack.push(row);
            });
                        
            response.json(sendBack);
    });
});

/* adds member to the database for fan club members */
app.post('/addMember', (req, res) => {
    const data = req.body;
    const fullName = data.fullName;
    const dob = data.dob;
    const email = data.email;
    const phone = data.phone;
    const password = data.password;
    const avatar = data.avatarValue;

    const sql_insert = `INSERT INTO members (email, name, dob, phoneNumber, password, avatar)
                            VALUES (?, ?, ?, ?, ?, ?)`;

    db.run(
        sql_insert, [email, fullName, dob, phone, password, avatar], (err) => {
            if (err) {
                return console.error(err.message);
            }

            console.log("Member added to the fan club database!");
    });
});