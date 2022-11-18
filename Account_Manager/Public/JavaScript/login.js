/* 
 * client side JavaScript for the login screen 
 */

/* password show/hide toggle */
function showPassword() {
    const showPass = document.getElementById('password');    

    if (showPass.type === "password") { /* if currently hidden */
        showPass.type = "text";
    } else { /* else currently shown */
        showPass.type = "password";
    }
}