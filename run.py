"""
Punto de entrada principal de la aplicación MediControl.
Ejecutar este archivo levanta el servidor de desarrollo de Flask.
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
