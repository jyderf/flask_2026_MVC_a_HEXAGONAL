from flask import Flask

from src.interface_adapters.controllers.productos_controller import (
  crear_blueprint_productos,
)
from src.interface_adapters.gateways.repositorios import (
  ImagenProductoMongo,
  ProductoMysql,
)

app = Flask(__name__, template_folder="src/templates")

app.register_blueprint(
  crear_blueprint_productos(ProductoMysql(), ImagenProductoMongo())
)

if __name__ == "__main__":
  app.run(debug=True)




