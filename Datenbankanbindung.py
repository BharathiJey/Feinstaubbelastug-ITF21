
import mysql
import mysql.connector


connection = mysql.connector.connect(host = "localhost",
                                     user = "admin",
                                     passwd = "root",
                                     db = "Sensorabfrage")

connection.close()