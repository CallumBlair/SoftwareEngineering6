//JavaScript


//Completes calls to the API using an XMLHttpRequest object
function callAPI(url, elResponse) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            let response = JSON.parse(this.responseText);
            document.getElementById(elResponse).value =  response.result;
        }

    }
    xhttp.open("GET", url, true);
    xhttp.send();
}

//Creates a new user
function NewUserFunc() {
	//Gets the needed values
	let userfirstname = document.getElementById("UserFName").value;
	let userlastname = document.getElementById("UserLName").value;
	let userpassword = document.getElementById("UserPassword").value;
	let username = document.getElementById("Username").value;
	//Creates URL string
	let urlStr = "/api/newuser?userfirstname=" + userfirstname + "&userlastname=" + userlastname + "&userpassword=" + userpassword + "&username=" + username;
	let outId = "UserFName";
	callAPI(urlStr , outId);
	document.getElementById("UserLName").value =  "";
	document.getElementById("UserPassword").value =  "";
	document.getElementById("Username").value =  "";

}
//Creates a new member
function NewMemberFunc() {
	//Gets the needed values
	let userfirstname = document.getElementById("memberFName").value;
	let userlastname = document.getElementById("memberLName").value;
	let userpassword = document.getElementById("memberPassword").value;
	let username = document.getElementById("postcode").value;
	//Creates URL string
	let urlStr = "/api/newmember?userfirstname=" + userfirstname + "&userlastname=" + userlastname + "&userpassword=" + userpassword + "&username=" + username;
	let outId = "memberFName";
	callAPI(urlStr , outId);
	document.getElementById("memberLName").value =  "";
	document.getElementById("memberPassword").value =  "";
	document.getElementById("postcode").value =  "";

}
//Creates a new book
function NewBookFunc() {
	//Gets the needed values
	let title = document.getElementById("book").value;
	let auth = document.getElementById("author").value;
	let isbn = document.getElementById("isbn").value;
	//Creates URL string
	let urlStr = "/api/newbook?title=" + title + "&author=" + auth + "&isbn=" + isbn;
	let outId = "book";
	callAPI(urlStr , outId);
	document.getElementById("author").value =  "";
	document.getElementById("isbn").value =  "";
}

//Searches for a book title from a book ID
function bookSearchFunc() {
	//Gets the needed value
	let id = document.getElementById("bookID").value;
	//Creates URL string
	let urlStr = "/api/booksearch?id=" + id;
	let outId = "bookID";
	callAPI(urlStr , outId);

}

//Searches for books from a specific author
function authSearchFunc() {
	//Gets the needed values
	let name = document.getElementById("authName").value;
	//Creates URL string
	let urlStr = "/api/authsearch?name=" + name;
	let outId = "authName";
	callAPI(urlStr , outId);
}

//Creates a new loan
function createLoanFunc() {
	//Gets the needed values
	let loanBookID = document.getElementById("loanBookID").value;
	let memberID = document.getElementById("memberID").value;
	let loanLength = document.getElementById("loanLength").value;
	//Creates URL string
	let urlStr = "/api/createloan?loanBookID=" + loanBookID + "&memberID=" + memberID + "&loanLength=" + loanLength;
	let outId = "loanBookID";
	callAPI(urlStr , outId);
	document.getElementById("memberID").value =  "";
	document.getElementById("loanLength").value =  "";
}

//Returns a loan
function returnLoanFunc() {
	//Gets the needed values
	let loanID = document.getElementById("loanID").value;
	//Creates URL string
	let urlStr = "/api/returnloan?loanID=" + loanID;
	let outId = "loanID";
	callAPI(urlStr , outId);

}


