import json
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_wtf.csrf import CSRFProtect
from forms import ItemForm  # Ajusta la ruta según la estructura de tu proyecto

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TU MADRE'

# Configuración de CSRF
csrf = CSRFProtect(app)

# Configuración de Flask-Login
login_manager = LoginManager(app)

# Modelo de usuario para Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Datos ficticios de usuario (reemplazar con tu lógica de autenticación)
users = {'admin': {'password': 'admin_password'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

items = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ItemForm()

    if request.method == 'POST' and form.validate_on_submit():
        nuevo_item = {
            'name': form.name.data,
            'description': form.description.data,
            'image': 'nombre_de_la_imagen.jpg',  # Reemplaza con la lógica real para manejar imágenes
            'link': form.link.data
        }
        items.append(nuevo_item)

    return render_template('index.html', form=form, items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))

    return render_template('logins.html')

@app.route('/eliminar/<int:item_index>', methods=['POST'])
@login_required  # Esta decoración requiere que el usuario esté autenticado
def eliminar(item_index):
    if current_user.is_authenticated and current_user.id == 'admin':
        if 0 <= item_index < len(items):
            del items[item_index]
    return redirect(url_for('index'))

@app.route('/newgame', methods=['GET', 'POST'])
def newgame():
    form = ItemForm()

    if request.method == 'POST' and form.validate_on_submit():
        nuevo_item = {
            'name': form.name.data,
            'description': form.description.data,
            'image': 'nombre_de_la_imagen.jpg',  # Reemplaza con la lógica real para manejar imágenes
            'link': form.link.data
        }
        items.append(nuevo_item)

    return render_template('newgame.html', form=form)

# Resto de las rutas...

if __name__ == '__main__':
    app.run(debug=True, port=3000)
