"""
Inicialización principal de la aplicación Flask.
Configura las extensiones y aplica el patrón Application Factory.
"""

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

migrate = Migrate()
db = SQLAlchemy()


def create_app():
    """
    Fábrica de la aplicación (Application Factory).
    Crea y configura la instancia de Flask, inicializa la base de datos
    y las migraciones, y registra los Blueprints para las diferentes rutas.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.medicos import bp as bp_medicos
    from app.blueprints.pacientes import bp as bp_pacientes
    from app.blueprints.citas import bp as bp_citas

    app.register_blueprint(bp_medicos, url_prefix='/medicos')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')

    @app.route('/')
    def index():
        """
        Ruta raíz de la aplicación.
        Redirige automáticamente al listado de médicos por defecto.
        """
        return redirect(url_for('medicos.listar'))

    return app
