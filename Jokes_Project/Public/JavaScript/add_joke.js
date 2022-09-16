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

/* submit form data */
function submit_data() {
    if (ensureChecked()) {
        alert("Submitting form");

        const first = document.getElementById('first_name').textContent;
        const last = document.getElementById('last_name').textContent;
        const orig = document.getElementsByName('original').values;
        const restricted = document.getElementsByName('friendly').values;
        const joke = document.getElementById('joke').textContent;

        const data = {first, last, orig, restricted, joke};
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        };
        fetch('/', options);
    } else {
        alert("Submitting form else");
    }
}
