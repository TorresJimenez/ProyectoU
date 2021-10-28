# import  sqlite3 
# from sqlite3 import Error 

# #conexion a la bd 

# def conexion():
#     url = "UniversidadDelRosarioDatabaseNumero1.db"
#     conn = sqlite3.connect(url)
#     return conn

# def insertNota(nota, retroalimentacion):
#     try:

#         conn = conexion()
#         conn.execute ("insert into prueba (nota,retrioalimentacion) values (?,?) ", (nota, retroalimentacion))
#         conn.commit()
#         conn.close()
#         return True
#     except Error as error:
#         return False

    
# def updateAsignatura():

#     try:
#         conn = conexion()
#         conn.execute ("insert into prueba (nombre) values (?) ", ())
#         conn.commit()
#         conn.close()
#         return True
#     except Error as error:
#         return False

# def list_Nota():
#     try:
#         conn = conexion()
#         conn.execute ("select * from prueba ")
#         conn.close()
#         return True
#     except Error as error:
#         return False


# def delete_Nota(id_nota):

#     try:
#         conn = conexion()
#         conn.execute ("delete into nota (idnota) values (?) ", (id_nota))
#         conn.commit()
#         conn.close()
#         return True
#     except Error as error:
#         return False