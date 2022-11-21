/* 
 * client side JavaScript for when a user logs in successfully 
 */

/* event listeners for admin forms */
const removeMemberForm = document.getElementById('remove_user');
removeMemberForm.addEventListener('submit', removeMember);

const promoteMemberForm = document.getElementById('promote_user');
promoteMemberForm.addEventListener('submit', promoteMember);

getMembers();

/* gets a list of all the members currently in the database */
async function getMembers() {
    const response = await fetch('/getMembers');
    const data = await response.json();
    const members = document.getElementById('club_members');
    
    /* add members from database to the web page */
    for (let i = 0; i < data.length; i++) {       
        /* create a row */
        let row = members.insertRow(1);

        /* identify columns of new row */
        let cell0 = row.insertCell(0);
        let cell1 = row.insertCell(1);
        let cell2 = row.insertCell(2);
        let cell3 = row.insertCell(3);
        let cell4 = row.insertCell(4);

        /* fill columns of new row */        
        cell0.textContent = `${data[i].name}`;
        cell1.textContent = `${data[i].email}`;
        cell2.textContent = `${data[i].dob}`;
        cell3.textContent = `${data[i].phoneNumber}`;
        cell4.textContent = `${data[i].status}`;
    }
}

/* retrieves user data when page loads */
window.onload = function() {
    var url = document.location.href;
    var params = url.split('?')[1].split('&');
    var data = {};
    var temp;

    for (let i = 0; i < params.length; i++) {
        temp = params[i].split('=');
        data[temp[0]] = temp[1];
    }

    processUserInfo(data.name);
}

/* processes the user info accordingly based on user info and privileges */
function processUserInfo(userInfo) {
    const userData = userInfo.split('%26');

    /* user name */
    const userNameLocation = document.getElementById('user_id');
    var userName = userData[0].replaceAll('%20', ' ');
    userNameLocation.innerText = userName;

    /* user avatar */
    const userAvatarLocationLeft = document.getElementById('avatar_left');
    const userAvatarLocationRight = document.getElementById('avatar_right');
    const img = document.createElement('img');
    const img2 = document.createElement('img');
    
    if (userData[1] == 0) { /* avatar id = 0 */
        img.src = "../Assets/avatar1.jpg";    
    } else if (userData[1] == 1) { /* avatar id = 1 */
        img.src = "../Assets/avatar2.png";
    } else if (userData[1] == 2) { /* avatar id = 2 */
        img.src = "../Assets/avatar3.jpg";
    } else if (userData[1] == 3) { /* avatar id = 3 */
        img.src = "../Assets/avatar4.png";
    } else { /* avatar id = 4 */
        img.src = "../Assets/avatar5.jpg";
    }

    img2.src = img.src;

    userAvatarLocationLeft.appendChild(img);
    userAvatarLocationRight.appendChild(img2);

    /* user status */
    const userStatusLocation = document.getElementById('user_priv');
    var userStatus = userData[2];
    userStatusLocation.innerText = userStatus;

    getPrivileges(userStatus);
}

/* provides access based on user privileges */
function getPrivileges(userStatus) {
    if (userStatus == "member") {
        var adminPrivs = document.getElementsByClassName('admin_status');

        for (let i = 0; i < adminPrivs.length; i++) {
            adminPrivs[i].style.display = 'none';
        }
    } 
}

/* admin promoting a member to admin status */
function promoteMember(e) {
    const promoteEmail = document.getElementById('emailPromote').value;

    const data = {promoteEmail};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/promoteMember', options);
    alert('User is set to admin status!');
    e.preventDefault();
}

/* admin removing a member from database */
function removeMember(e) {
    const removeEmail = document.getElementById('emailRemove').value;

    const data = {removeEmail};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/removeMember', options);
    alert('User removed from the club!');
    e.preventDefault();
}