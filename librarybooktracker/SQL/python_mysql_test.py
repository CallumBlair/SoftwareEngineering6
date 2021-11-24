import mysql.connector

mydb = mysql.connector.connect(
    host="s5330191.educationhost.cloud",
    user="tzjcgffq_admin ",
    password="Bournemouth1",
    database="tzjcgffq_libraryBookTracker"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT auth_name, author_id FROM auth_tbl")

myresult = mycursor.fetchall()

mycursor.close()

for x in myresult:
  print(x)
