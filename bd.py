import sqlite3

URL ="static/bd/Universidad_del_Rosario_Database.db"

def insertar(query,params)-> int:
    try:
        with sqlite3.connect(URL) as conn:
            warea = conn.cursor()
            rest = warea.execute(query,params).rowcount
            if rest !=0:
                conn.commit()
    except Exception as ex:
        rest =0
    finally:
            warea.close()
            conn.close()
    return rest

def consultar(query,params=None) ->list:
    try:
        with sqlite3.connect(URL) as conn:
            warea = conn.cursor()
            
            if params != None:
                rest =warea.execute(query,params).fetchall()
            else:
                rest =warea.execute(query).fetchall()
    except Exception as ex:
        rest = None
    finally:
            warea.close()
            conn.close()
    return rest

