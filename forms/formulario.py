from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField,DecimalField
from wtforms.validators import DataRequired

class RegistroPersona(FlaskForm):
    Nombre =StringField("Nombre",validators=[DataRequired ()])
    Apellidos =StringField("Apellidos",validators=[DataRequired ()])
    Email =StringField("Email",validators=[DataRequired ()])
    Telefono =IntegerField("Telefono",validators=[DataRequired ()])
    Genero =StringField("Genero",validators=[DataRequired ()])
    Rol=IntegerField("Rol (1-admin)(2-Docente)(3-estudiante)",validators=[DataRequired ()])
    User=StringField("User",validators=[DataRequired ()])
    password =PasswordField("Password",validators=[DataRequired ()])
    enviar =SubmitField("Registro")
    #editar =SubmitField("Editar")#para editar 
    eliminar =SubmitField("Eliminar")#para eleminar 
    #consultar =SubmitField("Consultar")#para eleminar 

class Login2(FlaskForm):
    User=StringField("Usuario",validators=[DataRequired ()])
    password =PasswordField("Contraseña",validators=[DataRequired ()])
    entrar =SubmitField("Entrar")

class Notas(FlaskForm):#registrar nota 
    id_actividad = IntegerField("codigo de la actividad ")
    id_estudiante= IntegerField("codigo de estudiante")
    Nota = DecimalField("calificacion  ")
    Retroalimentacion = StringField("Retroalimentacion")
    id_nota=IntegerField(" ingrese iD-nota PARA ELIMINAR   ")
    guardar = SubmitField("Guardar")
    eliminar  = SubmitField("Eliminar")

    

