"""
Blueprint para la gestión de Citas médicas.
Provee las rutas y controladores para las operaciones CRUD de la entidad Cita.
"""

from datetime import date, time

from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models.models import Cita, Medico, Paciente

bp = Blueprint('citas', __name__)

@bp.route('/')
def listar():
    """Obtiene y muestra todas las citas programadas ordenadas por fecha y hora."""
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template('citas/listar.html', citas=citas)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    """Renderiza el formulario para agendar una nueva cita y la guarda en la base de datos."""
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    if request.method == 'POST':
        cita = Cita(
            fecha=date.fromisoformat(request.form['fecha']),
            hora=time.fromisoformat(request.form['hora']),
            medico_id=int(request.form['medico_id']),
            paciente_id=int(request.form['paciente_id']),
        )
        db.session.add(cita)
        db.session.commit()
        return redirect(url_for('citas.listar'))
    return render_template('citas/form.html', cita=None, medicos=medicos, pacientes=pacientes)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Permite modificar los detalles de una cita existente (fecha, hora, médico o paciente)."""
    cita = Cita.query.get_or_404(id)
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    if request.method == 'POST':
        cita.fecha = date.fromisoformat(request.form['fecha'])
        cita.hora = time.fromisoformat(request.form['hora'])
        cita.medico_id = int(request.form['medico_id'])
        cita.paciente_id = int(request.form['paciente_id'])
        db.session.commit()
        return redirect(url_for('citas.listar'))
    return render_template('citas/form.html', cita=cita, medicos=medicos, pacientes=pacientes)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    """Cancela y elimina una cita médica de la base de datos dado su ID."""
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    return redirect(url_for('citas.listar'))
