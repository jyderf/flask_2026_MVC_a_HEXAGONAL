import pymysql

def get_mysql_connection():
  return pymysql.connect(
    host="localhost",
    user="root",
    password="123",
    database="mercancia",
    cursorclass=pymysql.cursors.DictCursor
  )