from SQL.sqlclass import *
def display(myresult): 
  if(myresult == []):
    print("Nothing Found: ")
  else:
    print("Found:")
    for x in myresult:
      print(x)

database = mydb()
###display(database.viewTable("active_loan_tbl")
##print(database.createLoan("0001", "10001"))
##display(database.viewTable("active_loan_tbl"))
##theid = int(input("hi: "))
##print(database.returnLoan(theid))
##display(database.viewTable("active_loan_tbl"))
##display(database.viewTable("past_loan_tbl"))
