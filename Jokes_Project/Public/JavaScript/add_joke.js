/* add joke to database */    
const fn = document.getElementById('first_name');
const ln = document.getElementById('last_name');
const orig = document.getElementsByName('original');
const restrict = document.getElementsByName('friendly');
const joke = document.getElementById('joke');

const data = {fn, ln, orig, restrict, joke};
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
};

fetch('/add', options);        

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