from src.config.mongo_connection import get_mongo_connection
from src.config.mysql_connection import get_mysql_connection


class ProductoMysql:

  @staticmethod
  def leer_productos():
    connection = get_mysql_connection()
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM producto AS p")
      datos = cursor.fetchall()
      connection.close()

    return datos


class ImagenProductoMongo:

  @staticmethod
  def leer_imagenes():
    db = get_mongo_connection()
    imagenes = list(db.producto.aggregate([
      {
        "$project": {
          "_id": 0
        }
      }
    ]))

    return imagenes


# 3. El repositorio cumple la promesa
"""Aquí sí hay SQL
 Aquí sí hay conexión"""