import sqlite3

def obtener_usuarios():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    lista_usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()

    return lista_usuarios


def verificar_usuario(usuario, contrasenia):
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sql = "SELECT * FROM usuarios WHERE nombre=? AND contrasenia=?"
    data = (usuario, contrasenia)
    cursor.execute(sql, data)
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado


def nueva_contrasenia(nueva_contrasenia, usuario):
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sql = "UPDATE usuarios SET contrasenia=? WHERE nombre=?"
    data = (nueva_contrasenia, usuario)
    cursor.execute(sql, data)
    conexion.commit()
    cursor.close()
    conexion.close()

