from typing import Protocol


class RepositorioProducto(Protocol):

  def leer_productos(self):
    ...


class RepositorioImagenProducto(Protocol):

  def leer_imagenes(self):
    ...

# 1. El dominio NO sabe nada de MySQL
"""Esto es puro, limpio, reutilizable"""


# 2. El puerto es una promesa

""" Dice: “alguien debe traer productos”
Pero no dice cómo"""