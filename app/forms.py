# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField

class ItemForm(FlaskForm):
    name = StringField('Nombre')
    description = TextAreaField('Descripción')
    image = FileField('Imagen')
    link = StringField('Enlace')
    submit = SubmitField('Agregar')


# También puedes tener un formulario simple para el login si lo prefieres
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')
