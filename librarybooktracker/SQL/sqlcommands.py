"""USAGE:
author = str(input("What Author: "))
command = findAuthorBooks(author)
myresult = runCommand(command, mydb)
"""



#runs the specified MySQL command, on the specified database
def runCommand(command, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

#Returns the books written by a given author
def findAuthorBooks(author):
    string = str("""
    SELECT b.book_title
    FROM book_tbl b, book_auth_lk lk, auth_tbl a
    WHERE b.book_isbn = lk.fk_book_id
    AND lk.fk_auth_id = a.author_id
    AND a.auth_name = '""") + author + "'"
    return string

#Returns a specified table
def viewTable(tableName):
    string = str("""
    SELECT * FROM """) + tableName
    return string
