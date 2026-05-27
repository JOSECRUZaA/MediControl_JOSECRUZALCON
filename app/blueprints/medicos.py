"""
Blueprint para la gestión de Médicos.
Provee las rutas y controladores para las operaciones CRUD de la entidad Medico.
"""

from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models.models import Medico

bp = Blueprint('medicos', __name__)

@bp.route('/')
def listar():
    """Lista todos los médicos registrados en la base de datos, ordenados por ID."""
    medicos = Medico.query.order_by(Medico.id).all()
    return render_template('medicos/listar.html', medicos=medicos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    """Muestra el formulario para crear un nuevo médico y procesa los datos enviados."""
    if request.method == 'POST':
        medico = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
        )
        db.session.add(medico)
        db.session.commit()
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/form.html', medico=None)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Muestra el formulario con los datos de un médico existente y actualiza sus valores."""
    medico = Medico.query.get_or_404(id)
    if request.method == 'POST':
        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        db.session.commit()
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/form.html', medico=medico)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    """Elimina un médico de la base de datos a partir de su ID."""
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for('medicos.listar'))
