"""
Definición de los modelos de base de datos utilizando SQLAlchemy.
Contiene las entidades principales del sistema: Medico, Paciente y Cita.
"""

from app import db

class Medico(db.Model):
    """
    Modelo que representa a un Médico en el sistema.
    Contiene información básica y la relación de las citas asignadas a este médico.
    """
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    especialidad = db.Column(db.String(120), nullable=False)
    citas = db.relationship('Cita', backref='medico', lazy=True)

class Paciente(db.Model):
    """
    Modelo que representa a un Paciente en el sistema.
    Contiene los datos de contacto y la relación de las citas que ha programado.
    """
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    citas = db.relationship('Cita', backref='paciente', lazy=True)

class Cita(db.Model):
    """
    Modelo que representa una Cita médica.
    Actúa como tabla intermedia (con datos extra) que relaciona un Médico y un Paciente
    en una fecha y hora específicas.
    """
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
