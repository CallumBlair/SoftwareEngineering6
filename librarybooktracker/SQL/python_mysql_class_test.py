from sqlclass import *
def display(myresult): 
  if(myresult == []):
    print("Nothing Found for the author: ")
  else:
    print("Found:")
    for x in myresult:
      print(x)

database = mydb()
#display(database.viewTable("active_loan_tbl")
print(database.createLoan("0001", "10001"))
