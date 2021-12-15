//JavaScript for new-book.html in templates folder

document.getElementById("BookButton").addEventListener("click", NewBookFunc)

function NewBookFunc() {
	let title = document.getElementById("Book").value;
	let info = "/api/newbook?title=" + title;
	apiNewBook(info); //starts a function to send information to flask
	
	console.log(title); //For testing purposes, delete later
	console.log(info); //For testing purposes, delete later
	
}

function apiNewBook(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}