"""

 Software Engineering 2021/22
 Assignment 2021 - Software Engineering Group Project
 Group 6 Library Book Tracker
 
"""


#Imports
from flask import Flask, render_template, jsonify, request, make_response
import sys, json
from SQL.sqlclass import * 

#Create a database object using default credentials
database = mydb()

#Create Flask instance
app = Flask(__name__)

#Landing page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#New Member page
@app.route("/new-member")
def newMember():
    return render_template("new-member.html")

@app.route("/api/newmember", methods = ['GET'])
def newMemberAPI():
    #Retrieve Variables from the GET request
    fName = request.args.get("userfirstname")
    sName = request.args.get("userlastname")
    pw = request.args.get("userpassword")
    postcode = request.args.get("username")
    
    #Create a full name string
    name = fName + " " + sName

    #Create new staff member
    ###########value = database.addStaff(name, pw, postcode)
    
    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": "ADDED"}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

#New Book Page
@app.route("/new-book")
def newBook():
    return render_template("new-book.html")

@app.route("/api/newbook", methods = ['GET'])
def newbookAPI():
    #Retrieve Variables from the GET request
    title = request.args.get("title")
    author = request.args.get("author")
    isbn = request.args.get("isbn")

    #######value = database.addBook(title,isbn,author)

    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": "ADDED"}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

#New User page
@app.route("/new-user")
def newUser():
    return render_template("new-user.html")

@app.route("/api/newuser", methods = ['GET'])
def newUserAPI():
    #Retrieve Variables from the GET request
    fName = request.args.get("userfirstname")
    sName = request.args.get("userlastname")
    pw = request.args.get("userpassword")
    postcode = request.args.get("username")
    name = fName + " " + sName
    
    #########value = database.addUser(name, pw, postcode)
    

    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": "ADDED"}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

#Manual Input Page
@app.route("/manual-input")
def loans():
    return render_template("loans.html")

@app.route("/api/createloan", methods = ['GET'])
def createLoanAPI():
    #Retrieve Variables from the GET request
    loanBookID = request.args.get("loanBookID")
    memberID = request.args.get("memberID")
    loanLength = request.args.get("loanLength")

    ########value = database.createLoan(loanBookID, memberID, None, loanLength)
    

    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": "Created"}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

@app.route("/api/returnloan", methods = ['GET'])
def returnLoanAPI():
    #Retrieve Variables from the GET request
    loanID = request.args.get("loanID")

    #######value = database.returnLoan(loanID)
    

    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": "Loan Returned"}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

#Data Search page
@app.route("/data-search")
def dataSearch():
    return render_template("data-search.html")

@app.route("/api/booksearch", methods = ['GET'])
def bookSearchAPI():
    #Retrieve Variables from the GET request
    bookId = request.args.get("id")

    value = database.bookTitle(bookId)
    
    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": value[0]}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

@app.route("/api/authsearch", methods = ['GET'])
def authSearchAPI():
    #Retrieve Variables from the GET request
    authName = request.args.get("name")

    value = database.findAuthorBooks(authName)
    
    #Create JSON Response
    response = make_response(
        jsonify(
            {"result": value}
        ),
    200,
    )
    response.headers["Content-Type"] = "application/json"
    #Return JSON Response
    return response

#Remove entry page
@app.route("/remove-entry")
def removeEntry():
    return render_template("remove-entry.html")

#Initialise Flask application
if __name__ == '__main__':
    app.run()
