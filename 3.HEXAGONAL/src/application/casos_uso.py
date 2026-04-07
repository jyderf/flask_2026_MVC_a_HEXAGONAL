from src.domain.puertos import RepositorioImagenProducto, RepositorioProducto


def listar_productos(repo_p: RepositorioProducto):
  return repo_p.leer_productos()


def listar_imagenes(repo_p: RepositorioImagenProducto):
  return repo_p.leer_imagenes()



# 4. El caso de uso es el cerebro
"""No sabe si usas MySQL, API, o archivos
 Solo ejecuta lógica"""
