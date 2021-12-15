//JavaScript for HTML in templates folder

function api(info) {
}

document.getElementById("LogInButton").addEventListener("click", LogInFunc)

function LogInFunc(){
	let username = document.getElementById("Username").value;
	let password = document.getElementById("Password").value;
	let info = "/api/login?username=" + username + "&password=" + password;
	api(info); //starts api function to send information to server
}