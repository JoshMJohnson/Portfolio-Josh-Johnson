/*
 * Client side JavaScript for add_joke page
 */

const form = document.getElementById('add_joke_form');
form.addEventListener('submit', addJoke);

/* ensure at least one checkbox is checked for appropriate age groups */
function ensureChecked() {
    const div = document.querySelector('#age_restricted');
    const checkboxes = div.querySelectorAll('input[type=checkbox]');
    const firstCheckbox = checkboxes.length > 0 ? checkboxes[0] : null;
    
    function init() {
        if (firstCheckbox) {
            for (let i = 0; i < checkboxes.length; i++) {
                checkboxes[i].addEventListener('change', checkValidity);
            }

            checkValidity();
        }
    }

    function isChecked() {
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                return true;
            }
        }

        return false;
    }

    function checkValidity() {
        const errorMessage = !isChecked() ? 'At least one checkbox must be selected.' : '';
        firstCheckbox.setCustomValidity(errorMessage);
    }
    
    init();
}; 

/* insert joke into the database */    
function addJoke() {
    const fn = document.getElementById('first_name').value;
    const ln = document.getElementById('last_name').value;
    const orig = document.querySelector('input[name="original"]:checked').value;

    /* get value of checked boxes within the checkbox age_restricted input */
    const restrict = [];
    const div = document.querySelector('#age_restricted');
    const checkboxes = div.querySelectorAll('input[type=checkbox]');

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            restrict.push(checkboxes[i].value);
        }
    }

    const joke = document.getElementById('joke').value;

    const data = {fn, ln, orig, restrict, joke};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/add', options);    
    alert("Joke was added to the database!!");    
}