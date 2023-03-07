from flask import Flask, redirect, request, url_for, jsonify, render_template
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

#----------------------------------------RUTAS-------------------------------------------------------------------------------------------------------------------

@app.route('/', methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'POST':
        alumn = Alumnos(nombre = create_form.nombre.data,
                        apellidos = create_form.apellidos.data,
                        email = create_form.email.data)
        db.session.add(alumn)
        db.session.commit()
    
    return render_template('index.html', name = 'Inicio', form = create_form)

@app.route('/ABCompleto', methods=['GET', 'POST'])
def abcompleto():
    create_form = forms.UserForm(request.form)
    #Select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos, name="ABCompleto")

@app.route('/modificar')
def modificar():
    create_form = forms.UserForm(request.form)
    id = request.args.get('id')
    #SELECT * FROM alumnos where id==id
    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    create_form.nombre.data = alumno.nombre
    create_form.apellidos.data = alumno.apellidos
    create_form.email.data = alumno.email
    
@app.route('/modificar', methods=['POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    id = request.args.get('id')
    #SELECT * FROM alumnos where id==id
    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    alumno.nombre = create_form.nombre.data
    alumno.apellidos = create_form.apellidos.data
    alumno.email = create_form.email.data

    db.session.add(alumno)
    db.session.commit()
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)