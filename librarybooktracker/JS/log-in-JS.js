//JavaScript for log-in.html in templates folder

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