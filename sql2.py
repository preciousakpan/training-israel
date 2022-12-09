import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "me",
    password = "you"
    )
print(mydb)
