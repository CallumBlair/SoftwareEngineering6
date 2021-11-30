import mysql.connector
from sqlcommands import *

mydb = mysql.connector.connect(
    host="s5330191.educationhost.cloud",
    user="tzjcgffq_admin",
    password="Bournemouth1",
    database="tzjcgffq_libraryBookTracker"
)

author = str(input("What Author: "))
command = findAuthorBooks(author)


myresult = runCommand(command, mydb)

if(myresult == []):
  print("Nothing Found for the author: "+ author)
else:
  print("Books found:")
  for x in myresult:
    print(x)
