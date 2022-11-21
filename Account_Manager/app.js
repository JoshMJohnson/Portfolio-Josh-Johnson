/* 
 * server side JavaScript for the Account Manager project 
 */
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

app.get('/create_account.html', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/create_account.html');
});

app.get('/logged_in.html', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/logged_in.html');
});

app.get('/login.html', (request, response) => {
    response.sendFile(__dirname + '/Public/HTML/login.html');
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
        email       STRING       PRIMARY KEY,
        name        STRING       NOT NULL,
        dob         DATE,
        phoneNumber VARCHAR (12),
        password    STRING       NOT NULL,
        avatar      INTEGER      NOT NULL,
        status      STRING       DEFAULT member
    );`
); */

/* retrieves all of the fan club members from the database during logged in process */
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

/* adds member to the database for fan club members during create account process */
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

/* verifies account exists and sends back details of user during login process */
app.post('/verifyAccount', (req, res) => {
    const data = req.body;
    const email = data.email;
    const password = data.password;

    const sql_query = `SELECT * 
                       FROM members
                       WHERE email = '${email}'
                       AND password = '${password}'`;
                       
    /* send user info from database to client side */
    var userInfo;

    db.all(
        sql_query, [], (err, rows) => {
            if (err) {
                return console.error(err.message);
            }
            
            rows.forEach((row) => {
                userInfo = row;
            });

            /* if no user exists in database */
            if (userInfo == undefined) {
                res.json(0);
            } else { /* else user found in database */
                res.json(userInfo);
            }
    });
});

/* promote a member status user to admin status */
app.post('/promoteMember', (req, res) => {
    const data = req.body;
    const emailAddress = data.promoteEmail;

    const sql_promote = `UPDATE members
                         SET status = 'admin'
                         WHERE email = '${emailAddress}'`;

    db.run(
        sql_promote, [], (err) => {
            if (err) {
                return console.error(err.message);
            }

            console.log("Member promoted to admin status!");
    });
});

/* remove a member from the database */
app.post('/removeMember', (req, res) => {
    const data = req.body;
    const emailAddress = data.removeEmail;

    const sql_remove = `DELETE FROM members
                        WHERE email = '${emailAddress}'`;

    db.run(
        sql_remove, [], (err) => {
            if (err) {
                return console.error(err.message);
            }

            console.log("User removed from database!");
    });
});