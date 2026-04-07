from flask import Blueprint, render_template, jsonify
from src.models.model_productos import Producto
from src.models.model_imagenes import ImagenProducto




productos_c = Blueprint(
  'productos_c',__name__,template_folder='../templates'
)


@productos_c.route("/productos")
def obtener_productos():
  data = Producto.leer_productos()    
  return render_template("productos.html",data = data)



@productos_c.route("/imagenes_productos")
def obtener_imagenes():
  data2 = ImagenProducto.leer_imagenes()
  #return jsonify(imagenes)
  return render_template("imagenes_productos.html",data2 = data2)