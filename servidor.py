from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

from flask_wtf import CSRFProtect

import os
import sqlite3

from utilidades import obtener_usuarios
from utilidades import verificar_usuario
from utilidades import nueva_contrasenia

app = Flask(__name__)
app.secret_key = os.urandom(24)
#csrf = CSRFProtect(app)
#<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"> 
# https://www.youtube.com/watch?v=kZ0x5K3msWg


# Pagina Maliciosa
"""
    <li>
      <a href="http://localhost:5500/pagina_maliciosa.html">Realiza esta encuesta y te damos 100 dolares</a>
    </li>

"""


@app.route('/')
def index():
    lista_usuarios = obtener_usuarios()
    return render_template('index.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasenia = request.form.get('contrasenia')

        resultado = verificar_usuario(usuario, contrasenia)

        if resultado is None:
            flash(message='Error, usuario o contrasenia incorrectos', category='error')
            return redirect('login')
        
        session['usuario'] = usuario
        return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


@app.route('/template_cambiar_contrasenia')
def template_cambiar_contrasenia():
    if 'usuario' in session:
        return render_template('cambiar_contrasenia.html')
    else:
        return redirect('login')


# Esta ruta simula una acción crítica (por ejemplo, cambiar la contraseña)
@app.route('/cambiar_contrasenia', methods=['POST'])
def cambiar_contrasenia():
    if 'usuario' in session:
        get_nueva_contrasenia = request.form.get('nueva_contrasenia')
        get_nombre_usuario = session['usuario']
        nueva_contrasenia(get_nueva_contrasenia, get_nombre_usuario)

        return redirect('/')
    else:
        return redirect('login')
    

if __name__ == '__main__':
    app.run(debug=True, host='localhost')