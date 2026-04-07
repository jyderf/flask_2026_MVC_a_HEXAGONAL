from flask import Flask, redirect, render_template, url_for
from pymongo import MongoClient
import pymysql

app = Flask(__name__, template_folder="src/templates")


def get_mysql_connection():
  return pymysql.connect(
    host="localhost",
    user="root",
    password="123",
    database="mercancia",
    cursorclass=pymysql.cursors.DictCursor
  )


def get_mongo_db():
  client = MongoClient("mongodb://localhost:27017/")
  return client["mercancia"]


@app.route("/")
def inicio():
  return redirect(url_for("obtener_productos"))


@app.route("/productos")
def obtener_productos():
  connection = get_mysql_connection()
  try:
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM producto AS p")
      data = cursor.fetchall()
  finally:
    connection.close()

  return render_template("productos.html", data=data)


@app.route("/imagenes_productos")
def obtener_imagenes():
  db = get_mongo_db()
  data2 = list(db.producto.aggregate([
    {
      "$project": {
        "_id": 0
      }
    }
  ]))
  return render_template("imagenes_productos.html", data2=data2)


if __name__ == "__main__":
  app.run(debug=True)