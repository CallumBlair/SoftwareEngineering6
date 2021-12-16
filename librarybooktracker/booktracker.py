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

@app.route("/login", methods=['GET','POST'])
def login():
     #Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['Username']
        password = request.form['Password']
        mycursor = self.mydb.cursor()
        mycursor.execute('SELECT * FROM staff_tbl WHERE staff_name = %s AND staff_pw = %s', (username, password,))
        # Fetch one record and return result
        account = mycursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
    return render_template("log-in.html")

@app.route("/datasearch")
def dataSearchView():
    return render_template("DataSearch.html")

@app.route("/manualinput")
def manualInputView():
    return render_template("ManualInput.html")

if __name__ == '__main__':
    app.run()
