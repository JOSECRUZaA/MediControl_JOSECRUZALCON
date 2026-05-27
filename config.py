import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Clase de configuración global de la aplicación.
    Define parámetros clave como la conexión a SQLite y configuraciones de seguridad.
    """
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/medicontrol.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
