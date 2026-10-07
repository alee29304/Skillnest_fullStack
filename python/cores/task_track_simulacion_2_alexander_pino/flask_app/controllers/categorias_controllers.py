from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.categoria import Categoria

@app.route('/categorias')
def ver_categorias():
    if 'usuario_id' not in session:
        return redirect('/login/vista')
    
    categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    return render_template('categorias.html', categorias=categorias)

@app.route('/categorias/nueva')
def nueva_categoria():
    if 'usuario_id' not in session:
        return redirect('/login/vista')
    return render_template('nueva_categoria.html')

@app.route('/categorias/crear', methods=['POST'])
def crear_categoria():
    if 'usuario_id' not in session:
        return redirect('/login/vista')

    if not Categoria.validar_categoria(request.form):
        return redirect('/categorias/nueva')

    data = {
        'nombre': request.form['nombre'],
        'usuario_id': session['usuario_id']
    }
    Categoria.guardar(data)
    return redirect('/categorias')

@app.route('/categorias/<int:id>/eliminar')
def eliminar_categoria(id):
    if 'usuario_id' not in session:
        return redirect('/login/vista')

    categoria = Categoria.obtener_por_id({'id': id})
    if categoria and categoria.usuario_id == session['usuario_id']:
        Categoria.eliminar({'id': id})

    return redirect('/categorias')