/*
 * Client side JavaScript for hear_jokes page
 */

const form = document.getElementById('hear_joke_form');
form.addEventListener('submit', hearJoke);

var personShowing = false;
var contentShowing = false;
var restrictedShowing = false;

/* display or hide the person text field */
function showHidePerson() {
    showHide("person", "person_div", "p");
}

/* display or hide the content text field */
function showHideContent() {
    showHide("related", "rel", "content");
}

/* display or hide the age restricted checkboxes */
function showHideRes() {
    showHide("restrictions", "age_restricted", "res");
}      

/* show or hide sections */
function showHide(id1, id2, element) {
    let restricted = document.getElementById(id1);

    /* if show age restricted checkboxes */
    if (restricted.value == "yes") {
        document.getElementById(id2).style.display = "block";

        /* if selecting display for age_restrictions */
        if (element == "res") {
            restrictedShowing = true;
        } else if (element == "content") { /* else if selecting display for content */
            contentShowing = true;
        } else if (element == "p") { /* else if selecting display for person */
            personShowing = true;
        }
    } else { /* else hide age restricted checkboxes */
        document.getElementById(id2).style.display = "none"; 

        /* if selecting display for age_restrictions */
        if (element == "res") {
            restrictedShowing = false;
        } else if (element == "content") { /* else if selecting display for content */
            contentShowing = false;
        } else if (element == "p") { /* else if selecting display for person */
            personShowing = false;
        }
    }  
}

/* allows the user to submit the form without requiring at least one box checked on invisible content */
function followThrough() {
    /* if specific person text field is showing */
    if (personShowing == true) {
        document.getElementById('person_field').required = true;
        const personField = document.getElementById('person_field').value;
    } else { /* else specific person text field is not showing */
        document.getElementById('person_field').required = false;
    }

    /* if content text field is showing */
    if (contentShowing == true) {
        document.getElementById('related_jokes').required = true;
        const contentField = document.getElementById('related_jokes').value;
    } else { /* else content text field is not showing */
        document.getElementById('related_jokes').required = false;
    }

    const restrict = [];

    /* gets values of age_restricted checkboxes to ensure one is checked if age_restricted boxes are showing */
    if (restrictedShowing == true) {
        const div = document.querySelector('#age_restricted');
        const checkboxes = div.querySelectorAll('input[type=checkbox]');

        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                restrict.push(checkboxes[i].value);
            }
        }
    } 
}

/* hear joke(s) from database */
function hearJoke() {    
    const specific = document.getElementById("person").value;
    const name = document.getElementById("person_field").value;
    const related = document.getElementById("related").value;
    const keyWords = document.getElementById("related_jokes").value;
    const original = document.getElementById("original").value;
    const restricted = document.getElementById("restrictions").value;
    const restrict = [];

    /* gets values of age_restricted checkboxes to ensure one is checked if age_restricted boxes are showing */
    if (restrictedShowing == true) {
        const div = document.querySelector('#age_restricted');
        const checkboxes = div.querySelectorAll('input[type=checkbox]');

        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                restrict.push(checkboxes[i].value);
            }
        }
    }

    const data = {specific, name, related, keyWords, original, restricted, restrict}; 
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    getData(options);
}

/* get data from database */
async function getData(options) {
    const response = await fetch('/hear', options);
    const responseData = await response.json();
    const listedJokes = document.getElementById('database_jokes');

    /* remove previous jokes listed if any */
    while (listedJokes.firstChild) {
        listedJokes.removeChild(listedJokes.firstChild);
    }
    
    /* add jokes requested from client to the web page */
    for (let i = 0; i < responseData.length; i++) {
        const li = document.createElement('li');
        const hr = document.createElement('hr');
        li.textContent = `${responseData[i].joke}`;
        listedJokes.appendChild(li);

        if (i != responseData.length - 1) {
            listedJokes.appendChild(hr);
        }
    }
}
