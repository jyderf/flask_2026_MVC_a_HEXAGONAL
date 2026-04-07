from typing import Protocol


class RepositorioProducto(Protocol):

  def leer_productos(self):
    ...


class RepositorioImagenProducto(Protocol):

  def leer_imagenes(self):
    ...
