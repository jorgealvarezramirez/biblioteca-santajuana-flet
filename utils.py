import os

def resource_path(relative_path):
    """Devuelve la ruta absoluta del recurso en un entorno normal (web/server)."""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
