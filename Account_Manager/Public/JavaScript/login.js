/* 
 * client side JavaScript for the login screen 
 */

const form = document.getElementById('login_form');
form.addEventListener('submit', login);

/* password show/hide toggle */
function showPassword() {
    const showPass = document.getElementById('password');    

    if (showPass.type === "password") { /* if currently hidden */
        showPass.type = "text";
    } else { /* else currently shown */
        showPass.type = "password";
    }
}

/* sends user to logged in page under correct account privileges */
function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const data = {email, password};

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    verifyAccount(options);
}

/* verifies account exists */
async function verifyAccount(options) {
    const response = await fetch('/verifyAccount', options);
    const responseData = await response.json();

    /* if no user exists in database with given info */
    if (responseData == 0) {
        alert('Incorrect email or password');
    } else { /* else user found in database */
        window.location.href = 'logged_in.html?name=' + encodeURIComponent(responseData.name + '&')
                                                      + encodeURIComponent(responseData.avatar + '&')
                                                      + encodeURIComponent(responseData.status);
    }
}