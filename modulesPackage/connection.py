import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="visit_my_city"
)

# import sqlite3
# mydb = sqlite3.connect("./visit_my_city.db", check_same_thread=False)
myCursor = mydb.cursor()
