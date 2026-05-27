"""
Blueprint para la gestión de Pacientes.
Provee las rutas y controladores para las operaciones CRUD de la entidad Paciente.
"""

from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models.models import Paciente

bp = Blueprint('pacientes', __name__)

@bp.route('/')
def listar():
    """Lista todos los pacientes registrados en la base de datos, ordenados por ID."""
    pacientes = Paciente.query.order_by(Paciente.id).all()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    """Muestra el formulario para registrar un nuevo paciente y procesa su guardado."""
    if request.method == 'POST':
        paciente = Paciente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
        )
        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/form.html', paciente=None)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Muestra el formulario con los datos de un paciente y actualiza su información."""
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/form.html', paciente=paciente)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    """Elimina un paciente de la base de datos a partir de su ID."""
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('pacientes.listar'))
