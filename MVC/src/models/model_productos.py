
from src.config.mysql_connection import get_mysql_connection

class Producto:

  @staticmethod
  def leer_productos():
    connection = get_mysql_connection()
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM producto AS p")
      datos = cursor.fetchall()
      connection.close()
      
    return datos