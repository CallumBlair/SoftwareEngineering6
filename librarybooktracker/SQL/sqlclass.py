"""USAGE:
database = mydb()
database.viewTable("active_loan_tbl")
"""

from SQL.secrets import *
import mysql.connector
#from mysql import connector as mysql
import datetime


class mydb():
    
    #Initialises class instance with imported values if non given
    def __init__(self,host=db_host, user=db_user,password=db_password, database=db_database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        #Calls create database
        self.createDB()
        
    #Creates a MySQL connection
    def createDB(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        
 ###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ###DATABASE Commands
        
    #runs the specified MySQL command
    def runCommand(self,command):
##        mycursor = self.mydb.cursor()
##        mycursor.execute(command)
##        myresult = mycursor.fetchall()
##        mycursor.close()
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute(command)
            myresult = mycursor.fetchall()
            mycursor.close()
        except:
            myresult = "Generic Error Message"
        return myresult
    
    #Commits changes
    def commit(self):
        self.runCommand("COMMIT;")

    #Returns the current date
    def currentDate(self):
        x = datetime.datetime.now()
        return x.strftime("%Y-%m-%d")
    
###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ###Query Functions
    
    #Returns the books written by a given author
    def findAuthorBooks(self,author):
        string = str("""
        SELECT b.book_title
        FROM book_tbl b, book_auth_lk lk, auth_tbl a
        WHERE b.book_isbn = lk.fk_book_id
        AND lk.fk_auth_id = a.author_id
        AND a.auth_name = '""") + author + "'"
        result = self.runCommand(string)
        return result

    #Lists all book instances and titles
    def findAllBooks(self):
        string = str("""
        SELECT i.book_id, b.book_title
        FROM instance_tbl i, book_tbl b
        WHERE i.fk_book_isbn = b.book_isbn""")
        result = self.runCommand(string)
        return result

    #Returns a specified table
    def viewTable(self,tableName):
        string = str("""
        SELECT * FROM """) + tableName
        result = self.runCommand(string)
        return result
    
    #Returns the number of a specific book the libary owns
    def findNumCopiesTitle(self,title):
        string = str("""
        SELECT * FROM (SELECT b.book_title AS bookisbn, COUNT(i.fk_book_isbn) AS counter
        FROM book_tbl b, instance_tbl i
        WHERE b.book_isbn = i.fk_book_isbn
        AND b.book_title =  '""") + title + """'GROUP BY b.book_title, i.fk_book_isbn
        ORDER BY counter) AS idtable;"""
        result = self.runCommand(string)
        return result
    
    #Returns the number of a specific book the libary owns
    def findNumCopiesISBN(self,isbn):
        string = str("""
        SELECT * FROM (SELECT b.book_title AS bookisbn, COUNT(i.fk_book_isbn) AS counter
        FROM book_tbl b, instance_tbl i
        WHERE b.book_isbn = i.fk_book_isbn
        AND b.book_isbn =  '""") + isbn + """'GROUP BY b.book_title, i.fk_book_isbn
        ORDER BY counter) AS idtable;"""
        result = self.runCommand(string)
        return result


    #Book Title from instance ID
    def bookTitle(self,bookId):
        string = str("""
        SELECT b.book_title 
        FROM book_tbl b, instance_tbl i
        WHERE i.book_id = """ + bookId + """
        AND b.book_isbn = i.fk_book_isbn;
        """)
        result = self.runCommand(string)
        return result

    #Template
    def template(self):
        string = str("""
        #SQL Here
        """)
        result = self.runCommand(string)
        return result

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ###Creation/Deletion Functions

    #Creates a new member of staff
    def addStaff(self, name, pw, postcode):
        string = str("""
        INSERT INTO staff_tbl(staff_name,staff_pw,staff_postcode) VALUES('""") + name + """','""" + pw + """', '""" + postcode + """');"""
        result = self.runCommand(string)
        self.commit()
        return result
        
    #Deletes a member of staff
    def deleteStaff(self, staff_id):
        string = str("""
        DELETE FROM staff_tbl WHERE staff_id =""") + str(staff_id)
        result = self.runCommand(string)
        self.commit()
        return result

    #Creates a new member
    def addMember(self, name, pw, postcode):
        string = str("""
        INSERT INTO member_tbl(member_name,member_pw,member_postcode) VALUES('""") + name + """','""" + pw + """', '""" + postcode + """');"""
        result = self.runCommand(string)
        self.commit()
        return result

    #Deletes a member
    def deleteMember(self, member_id):
        string = str("""
        DELETE FROM member_tbl WHERE member_id =""") + str(member_id)
        result = self.runCommand(string)
        self.commit()
        return result

    #Creates a new author with a new ID
    def addAuth(self, name):
        string = "SELECT author_id FROM auth_tbl"
        result = self.runCommand(string)
        #final_id = result[len(result)-1][0]
        final_id = int(0)
        for x in result:
            if int(x[0]) > final_id:
                final_id = int(x[0])
        new_id = final_id + 1
        string = """INSERT INTO auth_tbl(author_id, auth_name) VALUES('""" + str(new_id) + """','""" + name + """');""" 
        result = self.runCommand(string)
        self.commit()
        return result

    #Deletes an Author, REMOVE ALL LINKS PRIOR TO AUTHOR DELETION
    def deleteAuth(self, auth_id):
        string = str("""
        DELETE FROM auth_tbl WHERE author_id =""") + str(auth_id)
        result = self.runCommand(string)
        self.commit()
        return result

    #Gets the Author Id from the author name
    def getAuthId(self, auth_name):
        string = """SELECT author_id FROM auth_tbl WHERE auth_name = '""" + auth_name + """'"""
        print(string)
        result = self.runCommand(string)
        result = result[0][0]
        return int(result)
    
    ############ NEEDS MULTI AUTHOR SUPPORT ############
    #Creates a new book in the Book table and links it to an author 
    def addBook(self, bookTitle, bookIsbn, authName):
        auth_id = self.getAuthId(authName)
        string = """INSERT INTO book_tbl(book_title,book_isbn) VALUES('""" + bookTitle + """','""" + str(bookIsbn) + """');"""
        result = self.runCommand(string)
        string = """INSERT INTO book_auth_lk(fk_book_id,fk_auth_id) VALUES('""" + str(bookIsbn) + """','""" + str(auth_id) + """');"""
        result = self.runCommand(string)
        self.commit()
        return result

    #Removes a book from the book table
    def deleteBook(self, book_isbn):
        string = str("""DELETE FROM book_auth_lk WHERE fk_book_id = '""") + str(book_isbn) + """'"""
        print(string)
        result = self.runCommand(string)
        string = """DELETE FROM book_tbl WHERE book_isbn = '""" + str(book_isbn) + """'"""
        print(string)
        result = self.runCommand(string)
        self.commit()
        return result
        
    #Creates an instance of a book with a new ID
    def addInstance(self, book_isbn, book_status):
        string = "SELECT book_id FROM instance_tbl"
        result = self.runCommand(string)
        final_id = int(0)
        for x in result:
            if int(x[0]) > final_id:
                final_id = int(x[0])
        new_id = str(final_id + 1).zfill(4)
        string = """INSERT INTO instance_tbl(book_id,fk_book_isbn,book_status) VALUES('""" + new_id + """','""" + book_isbn + """','""" + book_status + """');"""
        result = self.runCommand(string)
        self.commit()
        return result
        
    #Deletes an instance of a book
    def deleteInstance(self,book_id):
        string = """DELETE FROM instance_tbl WHERE book_id = '""" + str(book_id) + """'"""
        result = self.runCommand(string)
        self.commit()
        return result

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ###Loans

    #Creates a new loan in the Active Loan Table  
    def createLoan(self, book_id, member_id, creation_date = None, loanPeriod = 14, returned = False):
        if creation_date == None:
            creation_date = self.currentDate()
        return_date = datetime.datetime.strptime(creation_date,"%Y-%m-%d")
        return_date = (return_date + datetime.timedelta(days=loanPeriod)).strftime("%Y-%m-%d")
        string = """INSERT INTO active_loan_tbl(book_id,member_id,creation_date,return_date,returned) VALUES ('""" + str(book_id) + """', '""" + str(member_id) + """', '""" + str(creation_date) + """',' """ + str(return_date) + """',""" + str(returned) + ")"
        result = self.runCommand(string)
        self.commit()
        return result
    
    #Sets the loan to returned and transfers it to the Past Loans table
    def returnLoan(self, loan_id):
        string = """UPDATE active_loan_tbl SET returned = true WHERE loan_id = '""" + str(loan_id) + """';"""
        result = self.runCommand(string)
        string = """INSERT INTO past_loan_tbl (loan_id, book_id,member_id, creation_date, return_date, returned) SELECT loan_id, book_id,member_id, creation_date, return_date, returned FROM active_loan_tbl WHERE loan_id = '""" + str(loan_id) + """';"""
        result = self.runCommand(string)
        string = """DELETE FROM active_loan_tbl WHERE loan_id = '""" + str(loan_id) + """';"""
        result = self.runCommand(string)
        self.commit()
        return result

    #Returns a past loan from a loan id
    def getPastLoan(self, loan_id):
        string = """SELECT * FROM past_loan_tbl WHERE loan_id = '""" + str(loan_id) + """';"""
        result = self.runCommand(string)
        return result

    #Returns all past loans associated with a specific book
    def getBookPastLoan(self, book_id):
        string = """SELECT * FROM past_loan_tbl WHERE book_id = '""" + str(book_id) + """';"""
        result = self.runCommand(string)
        return result

    #Returns a past loan from a member id
    def getMemberPastLoan(self, member_id):
        string = """SELECT * FROM past_loan_tbl WHERE member_id = '""" + str(member_id) + """';"""
        result = self.runCommand(string)
        return result

    #Returns an active loan from a loan id
    def getActiveLoan(self, loan_id):
        string = """SELECT * FROM active_loan_tbl WHERE loan_id = '""" + str(loan_id) + """';"""
        result = self.runCommand(string)
        return result

    #Returns an active loan associated with a book id
    def getBookActiveLoan(self, book_id):
        string = """SELECT * FROM active_loan_tbl WHERE book_id = '""" + str(book_id) + """';"""
        result = self.runCommand(string)
        return result

    #Returns an active loan from a member id
    def getMemberActiveLoan(self, member_id):
        string = """SELECT * FROM active_loan_tbl WHERE member_id = '""" + str(member_id) + """';"""
        result = self.runCommand(string)
        return result
