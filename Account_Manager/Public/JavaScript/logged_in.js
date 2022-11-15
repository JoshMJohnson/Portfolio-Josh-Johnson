/* 
 * client side JavaScript for when a user logs in successfully 
 */
getMembers();

/* gets a list of all the members currently in the database */
async function getMembers() {
    const response = await fetch('/members');
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