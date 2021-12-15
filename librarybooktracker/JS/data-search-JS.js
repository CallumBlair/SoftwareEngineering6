//JavaScript for data-search.html in templates folder

document.getElementById("SearchButton").addEventListener("click", DataSearch)

function DataSearch() {
	let bookid = document.getElementById("BookID").value;
	let memberid = document.getElementById("MemberID").value;
	let loanid = document.getElementById("LoanID").value;
	let userid = document.getElementById("UserID").value;
	let info = "/api/datasearch?bookid=" + bookid + "&memberid=" + memberid + "&loanid=" + loanid + "&userid=" + userid;
	apiDataSearch(info); //starts a function to send information to flask
	
	console.log(bookid + " " + memberid + " " + loanid + " " + userid); //For testing purposes, delete later
	console.log(info) //For testing purposes, delete later
}

function apiDataSearch(info) {
	let flask = new XMLHttpRequest();
	
	flask.open("GET", info, true);
	flask.send();
}