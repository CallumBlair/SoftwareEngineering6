from sqlclass import *

database = mydb()


author = str(input("What Author: "))
command = database.findAuthorBooks(author)
myresult = database.runCommand(command)

if(myresult == []):
  print("Nothing Found for the author: "+ author)
else:
  print("Books found:")
  for x in myresult:
    print(x)

