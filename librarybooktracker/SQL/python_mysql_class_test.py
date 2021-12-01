from sqlclass import *

def display(myresult): 
  if(myresult == []):
    print("Nothing Found for the author: ")
  else:
    print("Found:")
    for x in myresult:
      print(x)

database = mydb()
display(database.viewTable("auth_tbl"))
database.addAuth("Callum")
display(database.viewTable("auth_tbl"))
idd = int(input("ID"))
database.deleteAuth(idd)
display(database.viewTable("auth_tbl"))

