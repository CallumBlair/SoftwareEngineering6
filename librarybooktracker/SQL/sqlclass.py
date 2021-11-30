"""USAGE:
author = str(input("What Author: "))
command = findAuthorBooks(author)
myresult = runCommand(command, mydb)
"""
import mysql.connector
#from mysql import connector as mysql
class mydb():

    def __init__(self,host="s5330191.educationhost.cloud", user="tzjcgffq_admin",
                 password="Bournemouth1", database="tzjcgffq_libraryBookTracker"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.createDB()
        
    def createDB(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
 
    #runs the specified MySQL command, on the specified database
    def runCommand(self,command):
        mycursor = self.mydb.cursor()
        mycursor.execute(command)
        myresult = mycursor.fetchall()
        mycursor.close()
        return myresult

    #Returns the books written by a given author
    def findAuthorBooks(self,author):
        string = str("""
        SELECT b.book_title
        FROM book_tbl b, book_auth_lk lk, auth_tbl a
        WHERE b.book_isbn = lk.fk_book_id
        AND lk.fk_auth_id = a.author_id
        AND a.auth_name = '""") + author + "'"
        return string

    #Returns a specified table
    def viewTable(self,tableName):
        string = str("""
        SELECT * FROM """) + tableName
        return string
