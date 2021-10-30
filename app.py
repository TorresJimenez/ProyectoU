import json
import  bd 
from werkzeug.utils import escape

#GRUPO 8 
from flask import Flask, request, redirect ,flash,session
from flask import render_template 
from flask import render_template as render
#---------------------------para base de datos 
import sqlite3
import os

from forms.formulario import Login2, RegistroPersona, Notas
#------para encriptar----
import hashlib


#INSTANCIA  DE OBJETO FLASK 
app= Flask(__name__)

app.secret_key = os.urandom(20)

#login---------Usuario -----------
@app.route("/login",methods=["GET","POST"])
def login2():
    frm = Login2()
    if frm.validate_on_submit():
        User=frm.User.data
        password=frm.password.data 
        #cifrar contraseña 
        encrp=hashlib.sha256(password.encode('utf-8'))
        pass_enc=encrp.hexdigest()
        with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
            #crea un cursor
            con.row_factory = sqlite3.Row #anadir 
            cur=con.cursor()
            cur.execute("SELECT * FROM personaRegistro WHERE User = ? AND password =?",[User,pass_enc])
            row = cur.fetchone()
            if row:
                session["usuario"] = User #para saber si la persona esta autenticada
                session["perfil"] = row["Rol"]
                
                if row["Rol"] == 1:
                    return redirect("/perfiladministrador")
                elif row["Rol"] == 2:
                    return redirect("/perfildocente")
                elif row ["Rol"]== 3:
                    return redirect ("/perfilestudiante")
                else :
                    flash("No se identifica este acceso")  
            else:
                flash("Usuario/password Incorrectos")

    return render_template("login.html",frm=frm)


#-------------------------CRUD1-----------
#registar ----usuarios ,docnte,estudiante,administrativo
@app.route("/registrousuario",methods = ["GET","POST"])#Administrador 
def registrousuario():
    frm = RegistroPersona()
    if "usuario" in session: #pregunta si hay una sesion activa 
    
        if frm.validate_on_submit():
            
            Nombre =frm.Nombre.data
            Apellidos=frm.Apellidos.data
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
            with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
                #crea un cursor
                cur=con.cursor()
                #sentencia en sql
                cur.execute("INSERT INTO personaRegistro (Nombre, Apellidos, Email, Telefono, Genero, Rol, User, password) VALUES (?,?,?,?,?,?,?,?)",[Nombre, Apellidos, Email, Telefono, Genero, Rol, User,pass_enc] )
                #ejecuta la sentencia sql
                con.commit()
                flash("Registro exitoso")
                # return"Registro Guardado con exito <a href='/perfiladministrador'> Mi Perfil </a>"
        return render_template ("registroUsuario.html",frm=frm)
    else:
    	    return redirect ("/login")
      

#---------------
@app.route("/logout",methods = ["GET"])
def logout():
    session.clear()
    return redirect("/login")
#-----------
# @app.route("/eliminarusuario",methods=["GET","POST"])
# def eliminacionusuario():
#     frm = RegistroPersona()
  
#     cur=con.cursor()
#     row = cur.fetchone()
#     con.row_factory = sqlite3.Row
#     if "usuario" in session :
#     	if row:
                
#             session["perfil"] = row["Rol"]
                
#             if row["Rol"] == 1:
#                 if request.method == "POST":

#              	    User = frm.User.data

#              		with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:                   
#                         cur.execute("DELETE FROM personaRegistro WHERE User = ? ",[User])
#                         con.commit()
#                     flash("Usuario Eliminado")  
#                 return render_template("eliminar.html",frm=frm)
#             else :
#                 flash("No se identifica este acceso con el usuario")  
#     else:
#     	return redirect ("/login")


##------eliminarUsuario#-------------------------CRUD2-----------
@app.route("/eliminarusuario",methods=["GET","POST"])
def eliminacionusuario():
    frm = RegistroPersona()
    if "usuario" in session :
        if session ["Rol"]==1:
            if request.method == "POST":
              
                User = frm.User.data
              
                with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
                  
                    cur=con.cursor()
                    cur.execute("DELETE FROM personaRegistro WHERE User = ? ",[User])
                    con.commit()
                    flash("Usuario Eliminado")  
            return render_template("eliminar.html",frm=frm)
    else:
    	return redirect ("/login")
      

#---------------------consultar usuarios -----
@app.route("/consulta",methods=["GET","POST"])
def consultadeusuariosexistentes():
    if "usuario" in session :
        with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
            con.row_factory = sqlite3.Row
            cur=con.cursor()
            cur.execute("SELECT* FROM personaRegistro")
            rows = cur.fetchall()

      
            return render_template("listar_Consultar.html",rows=rows)
    else:
    	return redirect ("/login")
      

#-----registro notas# 
@app.route("/registroNota",methods = ["GET","POST"]) 
def registroNota():
    frm = Notas()
    if "usuario" in session :
        if frm.validate_on_submit():
            id_actividad=frm.id_actividad.data
            id_estudiante=frm.id_estudiante.data
            Nota=frm.Nota.data
            Retroalimentacion=frm.Retroalimentacion.data

            print ([id_actividad,id_estudiante,Nota,Retroalimentacion] )
            #conexion parala base de datos 
            with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
                #crea un cursor
                cur=con.cursor()
                #sentencia en sql
                cur.execute("INSERT INTO pruebaNota ( id_actividad,id_estudiante,Nota,Retroalimentacion) VALUES (?,?,?,?)",[id_actividad,id_estudiante,float(Nota),Retroalimentacion] )
                #ejecuta la sentencia sql
                con.commit()
                flash("Nota Guardada")

        return render_template ("registroNotas.html",frm=frm)
    else:
    	return redirect ("/login")
    
#-------------------------consulta nota  ----
@app.route("/consultanota_retro",methods=["GET","POST"])
def consultanota_retro():
    if "usuario" in session :
        with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
            con.row_factory = sqlite3.Row
            cur=con.cursor()
            cur.execute("SELECT* FROM pruebaNota")
            rows = cur.fetchall()

            return render_template("listar_Nota.html",rows=rows)
    else:
    	return redirect ("/login")
    

#------------------------------eliminar nota 

@app.route("/delete_nota", methods=["GET","POST"])
def delete_nota():
    frm = Notas()
    if "usuario" in session :
        if request.method == "POST":
            id_nota = escape(frm.id_nota.data)
            with sqlite3.connect("UniversidadDelRosarioDatabaseNumero1.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM pruebaNota WHERE id_nota = ?", [id_nota])
                con.commit()
                if con.total_changes > 0: #para verificar si realmente lo 
                    flash("Nota Eliminada")
                else:
                    flash("La nota NO se pudo eliminar")

        return render_template("Eliminar_Nota.html", frm=frm)
    else:
    	return redirect ("/login")







#--------resto de rutas----
@app.route("/",methods = ["GET"])
def home2 ():
    return render_template("index.html")

@app.route("/home",methods = ["GET"])#principal
def home ():
    return render_template("index.html")

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