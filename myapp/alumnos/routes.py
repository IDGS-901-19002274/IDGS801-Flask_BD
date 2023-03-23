from flask import Flask, Blueprint, request, render_template, url_for, redirect
from models import db, Alumnos
import forms

alumnos = Blueprint('alumnos', __name__)

# ---------------------------------------------------- GET ALL ---------------------------------------------------------------------------------------


@alumnos.route('/alumnos/index', methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    # Select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('index_alumno.html', form=create_form, alumnos=alumnos, name="Alumnos")

@alumnos.route('/alumnos/registrar', methods=['GET', 'POST'])
def registrar():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST':
        alumn = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data)
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template('registrar_alumno.html', name='Alumnos', form=create_form)

# ---------------------------------------------------- MODIFICAR --------------------------------------------------------------------------------------


@alumnos.route('/alumnos/modificar', methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        # SELECT * FROM alumnos where id==id
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumno.nombre
        create_form.apellidos.data = alumno.apellidos
        create_form.email.data = alumno.email

    if request.method == 'POST':
        id = create_form.id.data
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno.nombre = create_form.nombre.data
        alumno.apellidos = create_form.apellidos.data
        alumno.email = create_form.email.data
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template('modificar_alumno.html', name='Alumnos', form=create_form)
# ---------------------------------------------------- ELIMINAR --------------------------------------------------------------------------------------


@alumnos.route('/alumnos/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        # SELECT * FROM alumnos where id==id
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumno.nombre
        create_form.apellidos.data = alumno.apellidos
        create_form.email.data = alumno.email

    if request.method == 'POST':
        id = create_form.id.data
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno.nombre = create_form.nombre.data
        alumno.apellidos = create_form.apellidos.data
        alumno.email = create_form.email.data
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template('eliminar_alumno.html', name='Alumnos', form=create_form)