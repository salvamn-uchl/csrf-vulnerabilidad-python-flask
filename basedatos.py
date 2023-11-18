import sqlite3

conexion = sqlite3.connect('database.db')
#conexion.execute('CREATE TABLE usuarios (nombre TEXT, contrasenia TEXT)')

#cursor = conexion.cursor()
#cursor.execute('INSERT INTO usuarios (nombre, contrasenia) VALUES (?, ?)', ('tobias', '1234567'))
#conexion.commit()




conexion.close()

