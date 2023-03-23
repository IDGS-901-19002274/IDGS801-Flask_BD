from flask import Flask, Blueprint, request, render_template, url_for, redirect
import forms
import resistensias

resistencias = Blueprint('resistencias', __name__)

@resistencias.route('/resistencias/index')
def index():
    return render_template('resistencias.html', name = 'Resistencias')