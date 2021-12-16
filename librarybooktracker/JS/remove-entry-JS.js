//JavaScript for remove-entry.html in templates folder

document.getElementById("RemoveBButton").addEventListener("click", RemoveBook)

function RemoveBook() {
	let bookid = document.getElementById("BookID").value;
	let info = "/api/removebook?bookid=" + bookid;
	apiRemove(info); //starts a function to send information to flask
	
	console.log(bookid); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
}

document.getElementById("RemoveMButton").addEventListener("click", RemoveMember)

function RemoveMember() {
	let memberid = document.getElementById("MemberID").value;
	let info = "/api/removemember?memberid=" + memberid;
	apiRemove(info); //starts a function to send information to flask
	
	console.log(memberid); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
}

document.getElementById("RemoveUButton").addEventListener("click", RemoveUser)

function RemoveUser() {
	let userid = document.getElementById("UserID").value;
	let info = "/api/removeuser?userid=" + userid;
	apiRemove(info); //starts a function to send information to flask
	
	console.log(userid); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
}


function apiRemove(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}