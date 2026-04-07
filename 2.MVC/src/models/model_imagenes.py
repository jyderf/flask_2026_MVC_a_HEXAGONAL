
from src.config.mongo_connection import get_mongo_connection

class ImagenProducto:

  @staticmethod
  def leer_imagenes():
    db = get_mongo_connection()
    imagenes = list(db.producto.aggregate([
      {
        "$project":{
          "_id":0
        }
      }
    ]))
    
    return imagenes