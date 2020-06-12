import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "123"
)

mycursor.execute("USE mysql;")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)