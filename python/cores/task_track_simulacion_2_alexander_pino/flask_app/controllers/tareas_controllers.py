from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria

@app.route('/tareas')
def ver_tareas():
    if 'usuario_id' not in session:
        return redirect('/')

    data_user = {'usuario_id': session['usuario_id']}
    
    tareas = Tarea.obtener_por_usuario(data_user)
    proximas = Tarea.obtener_proximas_tareas(data_user)
    categorias = Categoria.obtener_por_usuario(data_user)

    # Métricas para el panel
    pendientes = sum(1 for t in tareas if t.estado == 'Pendiente')
    en_progreso = sum(1 for t in tareas if t.estado == 'En progreso')
    completadas = sum(1 for t in tareas if t.estado == 'Completada')

    resumen = {
        'total': len(tareas),
        'pendientes': pendientes,
        'en_progreso': en_progreso,
        'completadas': completadas
    }

    # CAMBIO AQUÍ: renderiza 'tareas.html' en lugar de 'dashboard.html'
    return render_template('tareas.html', tareas=tareas, proximas=proximas, categorias=categorias, resumen=resumen)

@app.route('/tareas/nueva')
def nueva_tarea():
    if 'usuario_id' not in session:
        return redirect('/')
    
    categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    return render_template('nueva_tarea.html', categorias=categorias)

@app.route('/tareas/crear', methods=['POST'])
def crear_tarea():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Tarea.validar_tarea(request.form):
        return redirect('/tareas/nueva')

    data = {
        'titulo': request.form['titulo'],
        'descripcion': request.form['descripcion'],
        'prioridad': request.form['prioridad'],
        'estado': request.form.get('estado', 'Pendiente'),
        'fecha_limite': request.form['fecha_limite'],
        'usuario_id': session['usuario_id'],
        'categoria_id': request.form['categoria_id']
    }
    Tarea.guardar(data)
    return redirect('/tareas')

@app.route('/tareas/<int:id>')
def ver_detalle_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')

    tarea = Tarea.obtener_por_id({'id': id})
    if not tarea or tarea.usuario_id != session['usuario_id']:
        return redirect('/tareas')

    return render_template('detalle_tarea.html', tarea=tarea)

@app.route('/tareas/<int:id>/completar', methods=['POST'])
def marcar_completada(id):
    if 'usuario_id' not in session:
        return redirect('/')

    tarea = Tarea.obtener_por_id({'id': id})
    if tarea and tarea.usuario_id == session['usuario_id']:
        Tarea.cambiar_estado({'id': id, 'estado': 'Completada'})

    return redirect(f'/tareas/{id}')

@app.route('/tareas/<int:id>/editar')
def editar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')

    tarea = Tarea.obtener_por_id({'id': id})
    if not tarea or tarea.usuario_id != session['usuario_id']:
        return redirect('/tareas')

    categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    return render_template('editar_tarea.html', tarea=tarea, categorias=categorias)

@app.route('/tareas/<int:id>/actualizar', methods=['POST'])
def actualizar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')

    if not Tarea.validar_tarea(request.form):
        return redirect(f'/tareas/{id}/editar')

    data = {
        'id': id,
        'titulo': request.form['titulo'],
        'descripcion': request.form['descripcion'],
        'prioridad': request.form['prioridad'],
        'estado': request.form['estado'],
        'fecha_limite': request.form['fecha_limite'],
        'categoria_id': request.form['categoria_id']
    }
    Tarea.actualizar(data)
    return redirect(f'/tareas/{id}')

@app.route('/tareas/<int:id>/eliminar')
def eliminar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')

    tarea = Tarea.obtener_por_id({'id': id})
    if tarea and tarea.usuario_id == session['usuario_id']:
        Tarea.eliminar({'id': id})

    return redirect('/tareas')