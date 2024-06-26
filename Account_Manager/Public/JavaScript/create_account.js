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
    const avatar = document.getElementsByName('avatar');

    /* get value of radio input for avatar */
    var avatarValue;

    for (let i = 0; i < avatar.length; i++) {
        if (avatar[i].checked) {
            avatarValue = avatar[i].value;
            break;
        }
    }

    /* add member to database */
    const data = {fullName, dob, email, phone, password, avatarValue};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    fetch('/addMember', options);
    alert('Account created!');
    document.getElementById('create_account').submit();
}

/* verifies user info is acceptable */
async function verifyNewAccount() {
    const emailAddress = document.getElementById('email').value;
    const data = {emailAddress};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    const response = await fetch('/checkEmailAddress', options);
    const responseData = await response.json();

    /* if a user already exists in database with given info */
    if (responseData != 0) {
        alert(`Account already exists for address:  ${responseData.email}`);
        return 1;
    } 

    return 0;
}

/* confirms that the password given is the same as confirm password value and meets criteria */
async function acceptablePassword() {
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

    let exists = await verifyNewAccount();

    /* verifies that email address is in correct format of an email address */
    var validateEmail = (emailVal) => {
        return emailVal.match(
          /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    };

    const emailVal = document.getElementById('email').value;

    if (exists == 0 && validateEmail(emailVal)) {
        createAccount();
    } 
}

/* provides custom error message for an invalid password */
function errorPasswordNotification(errorMessage) {
    const passwordBox = document.getElementById('password');
    passwordBox.setCustomValidity(errorMessage);
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