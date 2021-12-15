//JavaScript for HTML in templates folder

document.getElementById("LogInButton").addEventListener("click", LogInFunc)

function LogInFunc(){
	let username = document.getElementById("Username").value;
	let password = document.getElementById("Password").value;
	let info = "/api/login?username=" + username + "&password=" + password;
	apiLogIn(info); //starts api function to send information to flask
	
	console.log(username + "" + "" + password); //For testing purposes, delete later
}

function apiLogIn(info) { //used to send information to flask
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}

document.getElementById("MemberButton").addEventListener("click", NewMemFunc)

function NewMemFunc(){
	let name = document.getElementById("Member").value;
	let info = "/api/newmember?name=" + name;
	apiNewMem(info); //starts a function to send information to flask
	
	console.log(name); //For testing purposes, delete later
}

function apiNewMem(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}
