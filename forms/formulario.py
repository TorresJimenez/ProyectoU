from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class RegistroPersona(FlaskForm):
    Nombre =StringField("Nombre",validators=[DataRequired ()])
    Apellido =StringField("Apellido",validators=[DataRequired ()])
    Email =StringField("Email",validators=[DataRequired ()])
    Telefono =IntegerField("Telefono",validators=[DataRequired ()])
    Genero =StringField("Genero",validators=[DataRequired ()])
    Rol=StringField("Rol",validators=[DataRequired ()])
    User=StringField("User",validators=[DataRequired ()])
    password =PasswordField("Password",validators=[DataRequired ()])
    enviar =SubmitField("Registro")
    #editar =SubmitField("Editar")#para editar 
    eliminar =SubmitField("Eliminar")#para eleminar 
    #consultar =SubmitField("Consultar")#para eleminar 



class Login2(FlaskForm):
    User=StringField("User",validators=[DataRequired ()])
    password =PasswordField("Password",validators=[DataRequired ()])
    entrar =SubmitField("Entrar")

