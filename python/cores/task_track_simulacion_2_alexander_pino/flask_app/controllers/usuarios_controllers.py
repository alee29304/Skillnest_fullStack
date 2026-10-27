from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/tareas')
    return render_template('inicio.html')

@app.route('/login/vista')
def vista_login():
    if 'usuario_id' in session:
        return redirect('/tareas')
    return render_template('inicio_sesion.html')

@app.route('/registro/vista')
def vista_registro():
    if 'usuario_id' in session:
        return redirect('/tareas')
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect('/registro/vista')
    
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': password_hash
    }
    usuario_id = Usuario.guardar(data)
    session['usuario_id'] = usuario_id
    session['usuario_nombre'] = request.form['nombre']
    return redirect('/tareas')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.obtener_por_email({'email': request.form['email']})
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Credenciales inválidas.", "login")
        return redirect('/login/vista')
    
    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    return redirect('/tareas')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')