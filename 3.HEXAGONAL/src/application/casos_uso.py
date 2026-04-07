from src.domain.puertos import RepositorioImagenProducto, RepositorioProducto


def listar_productos(repositorio: RepositorioProducto):
  return repositorio.leer_productos()


def listar_imagenes(repositorio: RepositorioImagenProducto):
  return repositorio.leer_imagenes()
