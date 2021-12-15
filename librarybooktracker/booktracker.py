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
def index():
    return render_template("index.html")

@app.route("/datasearch")
def dataSearchView():
    return render_template("DataSearch.html")

@app.route("/manualinput")
def manualInputView():
    return render_template("ManualInput.html")

if __name__ == '__main__':
    app.run()
