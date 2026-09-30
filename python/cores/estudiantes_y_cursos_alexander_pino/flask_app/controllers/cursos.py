from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for
)

from flask_app.models.curso import Curso


# ==========================================================
# PÁGINA PRINCIPAL
# ==========================================================

@app.route("/")
def inicio():
    """
    Redirige la raíz hacia la página de cursos.
    """

    return redirect(
        url_for("cursos")
    )


# ==========================================================
# MOSTRAR TODOS LOS CURSOS
# ==========================================================

@app.route("/cursos")
def cursos():
    """
    Obtiene y muestra todos los cursos.
    """

    todos_los_cursos = Curso.get_all()


    return render_template(
        "cursos.html",
        cursos=todos_los_cursos
    )


# ==========================================================
# CREAR CURSO
# ==========================================================

@app.route(
    "/cursos/crear",
    methods=["POST"]
)
def crear_curso():
    """
    Recibe el nombre del curso
    y crea un nuevo registro.
    """

    nombre = request.form.get(
        "nombre",
        ""
    ).strip()


    if not nombre:

        return redirect(
            url_for("cursos")
        )


    data = {
        "nombre": nombre
    }


    Curso.save(data)


    return redirect(
        url_for("cursos")
    )


# ==========================================================
# MOSTRAR CURSO
# ==========================================================

@app.route(
    "/cursos/<int:id>"
)
def mostrar_curso(id):
    """
    Obtiene un curso y sus estudiantes.
    """

    curso = Curso.get_curso_con_estudiantes(id)


    if curso is None:

        return redirect(
            url_for("cursos")
        )


    return render_template(
        "mostrar_curso.html",
        curso=curso
    )
