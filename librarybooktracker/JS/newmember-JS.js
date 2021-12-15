//JavaScript for new-member.html in templates folder

document.getElementById("MemberButton").addEventListener("click", NewMemFunc)

function NewMemFunc() {
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