import json

#GRUPO 8 
from flask import Flask, request, redirect 
from flask import render_template 
from flask import render_template as render
#---------------------------para base de datos 
import sqlite3
import os

from forms.formulario import Login2, RegistroPersona
#------para encriptar----
import hashlib


#INSTANCIA  DE OBJETO FLASK 
app= Flask(__name__)

app.secret_key = os.urandom(20)

#-------------------------CRUD1-----------
#registar ----usuarios ,docnte,estudiante,administrativo
@app.route("/registrousuario",methods = ["GET","POST"])#Administrador 
def registrousuario():
    frm = RegistroPersona()
    if frm.validate_on_submit():
        
        Nombre =frm.Nombre.data
        Apellido=frm.Apellido.data
        Email=frm.Email.data
        Telefono=frm.Telefono.data
        Genero=frm.Genero.data
        Rol=frm.Rol.data
        User=frm.User.data
        password=frm.password.data
        #cifra la contraseña 
        encrp=hashlib.sha256(password.encode('utf-8'))
        pass_enc=encrp.hexdigest()
        #conexion parala base de datos 
        with sqlite3.connect("Universidad_del_rosario_database.db") as con:
            #crea un cursor
            cur=con.cursor()
            #sentencia en sql
            cur.execute("INSERT INTO persona (Nombre, Apellido, Email, Telefono, Genero, Rol, User, password) VALUES (?,?,?,?,?,?,?,?)",[Nombre, Apellido, Email, Telefono, Genero, Rol, User,pass_enc] )
            #ejecuta la sentencia sql
            con.commit()
            return"Registro Guardado con exito <a href='/perfiladministrador'> Mi Perfil </a>"

    return render_template ("registroUsuario.html",frm=frm)

#login---------
@app.route("/loginnuevo",methods=["GET","POST"])
def login2():
    frm = Login2()
    if frm.validate_on_submit():
        User=frm.User.data
        password=frm.password.data 
        #cifrar contraseña 
        encrp=hashlib.sha256(password.encode('utf-8'))
        pass_enc=encrp.hexdigest()
        with sqlite3.connect("Universidad_del_rosario_database.db") as con:
            #crea un cursor
            cur=con.cursor()
            cur.execute("SELECT * FROM persona WHERE User = ? AND password =?",[User,pass_enc])

            if cur.fetchone():
                return "Bienvenido(a)!!!!"
            else:
                return"Usuario/password Incorrectos"

    return render_template("loginNuevo.html",frm=frm)

#------eliminar#-------------------------CRUD2-----------
@app.route("/eliminarusuario",methods=["GET","POST"])
def eliminacionusuario():
    frm = RegistroPersona()
    if request.method == "POST":
        User = frm.User.data
        
        with sqlite3.connect("Universidad_del_rosario_database.db") as con:
            
            cur=con.cursor()
            cur.execute("DELETE FROM persona WHERE User = ? ",[User])
            con.commit()
            return "Usuario Eliminado"    

    return render_template("eliminar.html",frm=frm)
#---------------------
#-------------------------CRUD3-----------
@app.route("/consulta",methods=["GET","POST"])
def consultadeusuariosexistentes():
 
    with sqlite3.connect("Universidad_del_rosario_database.db") as con:
        con.row_factory = sqlite3.Row
        cur=con.cursor()
        cur.execute("SELECT* FROM persona")
        rows = cur.fetchall()

        return render_template("listar_Consultar.html",rows=rows)

    # return render_template("eliminar.html",frm=frm)



#--------resto de rutas----
@app.route("/registrousu",methods = ["GET"])#Administrador 
def registroUsu():
    
    return render_template ("regisUsu.html")


@app.route("/home",methods = ["GET"])#principal
def home ():
    return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])#login con diseño
def login ():
    return render_template("login.html")
    

@app.route("/perfiladministrador",methods = ["GET","POST"])#perfil admin
def adminregistro ():
    return render_template("Perfiladmin.html")


@app.route("/perfildocente",methods = ["GET","POST"])#perfildocente
def docente ():#perfil docente 
    return render_template("perfildocente.html")

@app.route("/perfilestudiante",methods = ["GET","POST"])#perfilestudiante
def estudiante ():#perfil estudiante
    return render_template("perfilestudiante.html")



@app.route("/indicadores",methods = ["GET","POST"])#indicadores administrador 
def indicadores ():
    return render_template("indicadores.html")


@app.route("/docente_calificar",methods = ["POST","GET"])#docente
def docentecalificar():
    return render_template("calificar.html")

@app.route("/docente_comentar",methods = ["POST","GET"])#docente comentar actividad 
def comentar():
    return render_template ("Retroalimentacion.html")


@app.route("/estudiante_vernota",methods = ["POST","GET"])#Estudiante ver notas 
def estudiantevernota():
  return render_template ("ver_calificacion.thml")
 
@app.route("/estudiante_vercomen",methods = ["GET"])#Estudiante ver comentarios 
def estudiantevercomen():
    return render_template("ver_retroalimentacion.html")

@app.route("/regisActividad",methods = ["GET"])#docente registar actividad 
def regisActividad():
  return render_template ("regisActividad.html")

if __name__ == "__main__":
    app.run(debug=True)