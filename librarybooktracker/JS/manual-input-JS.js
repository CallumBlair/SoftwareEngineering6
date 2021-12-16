//JavaScript for manual-input.html in templates folder

document.getElementById("AddUpdate").addEventListener("click", ManInput)

function ManInput() {
	let bookid = document.getElementById("BookID").value;
	let memberid = document.getElementById("MemberID").value;
	let status = document.getElementById("BookStatus").value;
	let info = "/api/maninput?bookid=" + bookid + "&memberid=" + memberid + "&status=" + status;
	apiManInput(info); //starts a function to send information to flask
	
	console.log(bookid + " " + memberid + " " + status); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
}

function apiManInput(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}