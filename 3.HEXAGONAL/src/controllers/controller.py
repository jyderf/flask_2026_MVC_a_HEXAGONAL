from flask import Blueprint, render_template

from src.application.casos_uso import listar_imagenes, listar_productos
from src.domain.puertos import RepositorioImagenProducto, RepositorioProducto


def crear_blueprint_productos(
  repositorio_producto: RepositorioProducto,
  repositorio_imagen: RepositorioImagenProducto,
):
  productos_c = Blueprint(
    'productos_c', __name__, template_folder='../templates'
  )

  @productos_c.route("/productos")
  def obtener_productos():
    data = listar_productos(repositorio_producto)
    return render_template("productos.html", data=data)

  @productos_c.route("/imagenes_productos")
  def obtener_imagenes():
    data2 = listar_imagenes(repositorio_imagen)
    return render_template("imagenes_productos.html", data2=data2)

  return productos_c






