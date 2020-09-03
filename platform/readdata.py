import mysql.connector
import csv
from mysql.connector import Error

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "123"
)

# Get Daily Average Value for she SOil Moisture at Depth 1
mycursor =mydb.cursor()
mycursor.execute("USE lab;")

mycursor.execute('SELECT AVG(CASE attrName WHEN "soilMoistureCalibratedDepth1" THEN attrValue END)'
 'FROM `urn_ngsi-ld_SoilProbe_1_SoilProbe` WHERE DATE(recvTime) = CURDATE()'
 )

x = mycursor.fetchone() # Fetch the resulting value
print(x[0]+2, x[0]) # Example to extract this data to python
mycursor.close()