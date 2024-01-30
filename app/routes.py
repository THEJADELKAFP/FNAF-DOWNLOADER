# app/routes.py
from flask import Flask, render_template

app = Flask(__name__)

from .forms import ItemForm  # Ajusta la ruta según la estructura de tu proyecto

@app.route('/')
def index():
    form = ItemForm()  # Utiliza el nombre correcto de la clase del formulario
    items = []  # Inicializa items según tu lógica de negocio

    return render_template('index.html', form=form, items=items)
