def findAuthorBooks(author):
    string = str("""
    SELECT b.book_title
    FROM book_tbl b, book_auth_lk lk, auth_tbl a
    WHERE b.book_isbn = lk.fk_book_id
    AND lk.fk_auth_id = a.author_id
    AND a.auth_name = '""") + author + "'"
    return string

def runCommand(command, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
