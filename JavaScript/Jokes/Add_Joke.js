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

