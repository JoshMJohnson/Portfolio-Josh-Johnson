/* 
 * client side JavaScript for when a user creates a new account 
 */

/* creates a new member account */
function createAccount() {
    /* collect values given by user */
    const fullName = document.getElementById('full_name').value;
    const dob = document.getElementById('birth_date').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const avatar = document.getElementsByClassName('avatar').value;

    /* add member to database */
    


    document.getElementById('create_account').submit();
}

/* confirms that the password given is the same as confirm password value and meets criteria */
function acceptablePassword() {
    let goodCapital = false;
    let goodSpecial = false;
    let goodNumber = false;

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    /* password and confirm password is the same value */
    if (password.valueOf() != confirmPassword.valueOf()) {
        errorPasswordNotification('Passwords do not match');
        return;
    }

    /* loop through the password given */
    for (let i = 0; i < password.length; i++) {
        let asciiValue = password.charCodeAt(i);

        if (asciiValue >= 65 && asciiValue <= 90) { /* if character is a capital letter */
            goodCapital = true;
        } else if (asciiValue == 33 || asciiValue == 35 || asciiValue == 36 || asciiValue == 64 
                    || asciiValue == 37 || asciiValue == 126 || asciiValue == 38) { /* else if character is a special character */
            goodSpecial = true;
        } else if (asciiValue >= 48 && asciiValue <= 57) { /* else if character is a number */
            goodNumber = true;
        }
    }

    /* given password meets criteria */
    if (password.length < 8) { /* if less than 8 characters long */
        errorPasswordNotification("Must have 8 or more characters");
        return;
    } else if (!goodCapital) { /* else if no captial letters used */
        errorPasswordNotification("Must have at least one capital letter");
        return;
    } else if (!goodSpecial) { /* else if no special charaters used */
        errorPasswordNotification("Must have at least one special character (!, #, $, @, %, ~, &)");
        return;
    } else if (!goodNumber) { /* else if no numbers used */
        errorPasswordNotification("Must have at least one number");
        return;
    }

    createAccount();
}

/* password show/hide toggle */
function showPassword() {
    const showPass = document.getElementById('password');    
    const showConfirm = document.getElementById('confirm_password');

    if (showPass.type === "password") { /* if currently hidden */
        showPass.type = "text";
        showConfirm.type = "text";
    } else { /* else currently shown */
        showPass.type = "password";
        showConfirm.type ="password";
    }
}

/* provides custom error message */
function errorPasswordNotification(errorMessage) {
    const passwordBox = document.getElementById('password');
    passwordBox.setCustomValidity(errorMessage);
}