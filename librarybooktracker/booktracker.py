"""
 Software Engineering 2021/22
 Assignment 2021 - Software Engineering Group Project
        Library Book Tracker
"""

from flask import Flask, render_template

from SQL.sqlclass import * 

#database = mydb()


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/new-member")
def newMember():
    return render_template("new-member.html")


@app.route("/new-book")
def newBook():
    return render_template("new-book.html")

@app.route("/new-user")
def newUser():
    return render_template("new-user.html")

@app.route("/manual-input")
def manualInput():
    return render_template("manual-input.html")

@app.route("/data-search")
def dataSearch():
    return render_template("data-search.html")

@app.route("/remove-entry")
def removeEntry():
    return render_template("remove-entry.html")


if __name__ == '__main__':
    app.run()
