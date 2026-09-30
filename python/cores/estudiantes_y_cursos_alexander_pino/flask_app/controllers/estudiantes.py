from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for
)

from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


# ==========================================================
# FORMULARIO NUEVO ESTUDIANTE
# ==========================================================

@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    """
    Obtiene todos los cursos para mostrarlos
    dentro del select del formulario.
    """

    cursos = Curso.get_all()


    return render_template(
        "nuevo_estudiante.html",
        cursos=cursos
    )


# ==========================================================
# CREAR ESTUDIANTE
# ==========================================================

@app.route(
    "/estudiantes/crear",
    methods=["POST"]
)
def crear_estudiante():
    """
    Recibe los datos del formulario
    y crea un nuevo estudiante.
    """

    nombre = request.form.get(
        "nombre",
        ""
    ).strip()


    apellido = request.form.get(
        "apellido",
        ""
    ).strip()


    edad = request.form.get(
        "edad",
        ""
    ).strip()


    curso_id = request.form.get(
        "curso_id",
        ""
    ).strip()


    if not nombre or not apellido or not edad or not curso_id:

        return redirect(
            url_for("nuevo_estudiante")
        )


    try:

        edad = int(edad)
        curso_id = int(curso_id)

    except ValueError:

        return redirect(
            url_for("nuevo_estudiante")
        )


    data = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso_id": curso_id
    }


    Estudiante.save(data)


    return redirect(
        url_for("cursos")
    )
