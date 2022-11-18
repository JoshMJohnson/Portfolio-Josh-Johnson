/* 
 * client side JavaScript for the login screen 
 */

const form = document.getElementById('login_form');
form.addEventListener('submit', verifyAccount());

/* password show/hide toggle */
function showPassword() {
    const showPass = document.getElementById('password');    

    if (showPass.type === "password") { /* if currently hidden */
        showPass.type = "text";
    } else { /* else currently shown */
        showPass.type = "password";
    }
}

/* verifies account exists */
function verifyAccount() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    
}

/* sends user to logged in page under correct account privileges */
function login() {

}