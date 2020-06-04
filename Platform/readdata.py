import mysql.connector

cnx = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='lab')
cnx.close()