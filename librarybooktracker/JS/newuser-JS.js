//JavaScript for new-user.html in templates folder

document.getElementById("UserButton").addEventListener("click", NewUserFunc)

function NewUserFunc() {
	let userfirstname = document.getElementById("UserFName").value;
	let userlastname = document.getElementById("UserLName").value;
	let userpassword = document.getElementById("UserPassword").value;
	let username = document.getElementById("Username").value;
	let info = "/api/newuser?userfirstname=" + userfirstname + "&userlastname=" + userlastname + "&userpassword=" + userpassword + "&username=" + username;
	apiNewUser(info); //starts a function to send information to flask
	
	console.log(userfirstname + " " + userlastname + " " + userpassword + " " + username); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
}

function apiNewUser(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}