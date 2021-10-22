import json

#ultimo con indicadores 
from flask import Flask  , request, redirect 
from flask import render_template 
from flask import render_template as render
from bd import insertar, consultar

#INSTANCIA  DE OBJETO FLASK 
app= Flask(__name__)

@app.route("/home",methods = ["GET"])#principal
def home ():
    return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])#login
def login ():
    return render_template("login.html")
    

@app.route("/perfiladministrador",methods = ["GET","POST"])#perfil admin
def adminregistro ():
    return render_template("Perfiladmin.html")


@app.route("/perfildocente",methods = ["GET","POST"])
def docente ():#perfil docente 
    return render_template("perfildocente.html")

@app.route("/perfilestudiante",methods = ["GET","POST"])
def estudiante ():#perfil estudiante
    return render_template("perfilestudiante.html")



@app.route("/indicadores",methods = ["GET","POST"])
def indicadores ():#indicadores 
    return render_template("indicadores.html")
    
#-------------------------CRUD-----------
#1=administrador 2=docente 3=estudiante 4:asignatura
#5 actividad /1-4:taller,quiz,examen,trabajo,

#1-----consultar ------
lista_Asignatura={
        401:'costos',
        402:'administracion',
        403:'economia',
        404:'contabilidad',
        405:'finanza'
    }

lista_Asignatura_matriculadas= {
        301:[401,402],
        302:[402,405],
        303:[403,402],
        304:[404,405],
        305:[405,401],
    }


lista_Actividad= {
    501:{"descripcion ":'pdf', "titulo":'taller'},
    502:{"descripcion":'pdf', "titulo":'examen'},
    503:{"descripcion":'pdf', "titulo":'taller'},
    504:{"descripcion":'pdf', "titulo":'taller'},
    505:{"descripcion":'pdf', "titulo":'quiz'},
    506:{"descripcion":'pdf', "titulo ":'trabajo'},
}
#---------------------------
@app.route("/consulta")#envio1 peticion consulta
def consultar():
    return render_template("Consultar.html")

@app.route("/respuestaconsulta",methods=["POST"])
def consultarEstudiante_post():#consulta
    identificador = request.form["id"]
    nombre = request.form["nombre"]

   

    id=int(identificador)
    if id in lista_Asignatura_matriculadas:# Está matriculado y la materia 
        
        return f" 1( El estudiante esta matriculado, nombre ingresado {nombre},    2(Tiene matriculada la asignatura {lista_Asignatura_matriculadas[id]},     3(lista general de asignaturas {lista_Asignatura}"  
    else :
        return "el estudiante no esta matriculado "

#fin consulta----
# 2---------crear  -------       
@app.route("/materias_creadas",methods=["GET"])
def verMaterias():
    return " se creo la materia"

@app.route("/materia_crear",methods=["GET","POST"])#envio peticion crear 
def materia_crear():
    global lista_materia 
    
    if request.method=="GET":
        return render("Crear.html")
    elif request.method=="POST":
        id = request.values["id"]
        nombre = request.values["nombre"]
        lista_Asignatura [ len(lista_Asignatura)]= {"id":id, "nombre":nombre}
    else:
        return "no se creo la materia"

    return redirect('/materias_creadas')
#fin crear--------

#3--Eliminar---------

@app.route("/eliminacion_Asignatura",methods=["GET"])
def eliminacionAsignatura():
    return " se elimino la materia"

@app.route("/eliminar_Asignatura",methods=["DELETE"])
def eliminarAsignatura():
    id = request.values["id_eliminar"] 
    if id in lista_Asignatura: 
        del lista_Asignatura[id]
    return redirect ("/eliminacion_Asignatura")
#----- fin eliminar ---------
#4 ------crear actividad --------
@app.route("/docente_asig_acti",methods = ["GET"])#docente
def docenteasigacti ():
    return "se añadio actividad "


@app.route("/Actividad_crear",methods=["GET","POST"])#peticion crear actividad  
def Actividad_crear():
    global lista_Actividad 
    
    if request.method=="GET":
        return render("AsignarActividad.html")
    elif request.method=="POST":
        id = request.values["id"]
        descripcion = request.values["descripcion"]
        titulo = request.values["titulo"]
        lista_Actividad [ len(lista_Actividad)]= {"id":id, "descripcion":descripcion,"titulo":titulo  }
    else:
        return "no se creo la Actividad "

    return redirect('/docente_asig_acti')

#--------resto de rutas----


@app.route("/docente_calificar",methods = ["POST","GET"])#docente
def docentecalificar():
    return render_template("Calificar.html")

@app.route("/docente_comentar",methods = ["POST","GET"])#docente/lista
def comentar():
    return render_template ("Retroalimentacion.html")


@app.route("/estudiante_vernota",methods = ["GET"])#Estudiante
def estudiantevernota():
  return render_template ("ver_calificacion.thml")
 
@app.route("/estudiante_vercomen",methods = ["GET"])#Estudiante
def estudiantevercomen():
    return render_template("ver_retroalimentacion.html")





