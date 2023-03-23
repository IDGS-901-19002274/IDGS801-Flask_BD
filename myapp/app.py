from flask import Flask, redirect, request, url_for, jsonify, render_template
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

from alumnos.routes import alumnos
from resistencias.routes import resistencias

# ----------------------------------------RUTAS-------------------------------------------------------------------------------------------------------------------


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('alumnos.index'))

# ***************************************************** ALUMNOS *********************************************************


# ***************************************************** MAESTROS *********************************************************

app.register_blueprint(alumnos)
app.register_blueprint(resistencias)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)  # host='10.1.1.11',
