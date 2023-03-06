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
        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)