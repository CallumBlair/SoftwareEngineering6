"""
 Software Engineering 2021/22
 Assignment 2021 - Software Engineering Group Project
        Library Book Tracker
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

if __name__ == '__main__':
    app.run()
