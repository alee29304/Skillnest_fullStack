from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.usuario import Usuario
import bcrypt
import re
from datetime import date


usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/")
def index():
    return render_template("index.html")


@usuarios_bp.route("/registrar", methods=["POST"])
def registrar():

    nombre = request.form["nombre"].strip()
    apellido = request.form["apellido"].strip()
    email = request.form["email"].strip()
    password = request.form["password"]
    confirmar_password = request.form["confirmar_password"]
    fecha_nacimiento = request.form["fecha_nacimiento"]
    ciudad = request.form["ciudad"]
    genero = request.form.get("genero")
    intereses = request.form.getlist("intereses")

    errores = []

    # ==============================
    # VALIDAR NOMBRE
    # ==============================

    if not nombre:
        errores.append("El nombre es obligatorio.")
    elif len(nombre) < 2:
        errores.append("El nombre debe tener al menos 2 caracteres.")
    elif not nombre.isalpha():
        errores.append("El nombre solo puede contener letras.")

    # ==============================
    # VALIDAR APELLIDO
    # ==============================

    if not apellido:
        errores.append("El apellido es obligatorio.")
    elif len(apellido) < 2:
        errores.append("El apellido debe tener al menos 2 caracteres.")
    elif not apellido.isalpha():
        errores.append("El apellido solo puede contener letras.")

    # ==============================
    # VALIDAR EMAIL
    # ==============================

    email_regex = re.compile(
        r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

    if not email:
        errores.append("El e-mail es obligatorio.")
    elif not email_regex.match(email):
        errores.append("El e-mail no tiene un formato válido.")
    elif Usuario.buscar_por_email(email):
        errores.append("El e-mail ya está registrado.")

    # ==============================
    # VALIDAR CONTRASEÑA
    # ==============================

    if not password:
        errores.append("La contraseña es obligatoria.")
    elif len(password) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    elif not re.search(r"[A-Z]", password):
        errores.append(
            "La contraseña debe contener al menos una letra mayúscula."
        )
    elif not re.search(r"\d", password):
        errores.append(
            "La contraseña debe contener al menos un número."
        )

    # ==============================
    # CONFIRMAR CONTRASEÑA
    # ==============================

    if password != confirmar_password:
        errores.append("Las contraseñas no coinciden.")

    # ==============================
    # FECHA DE NACIMIENTO
    # ==============================

    if not fecha_nacimiento:
        errores.append("La fecha de nacimiento es obligatoria.")
    else:
        try:
            fecha_nac = date.fromisoformat(fecha_nacimiento)
            hoy = date.today()

            edad = hoy.year - fecha_nac.year

            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1

            if edad < 18:
                errores.append(
                    "Debes ser mayor de 18 años para registrarte."
                )

        except ValueError:
            errores.append("La fecha de nacimiento no es válida.")

    # ==============================
    # VALIDAR CIUDAD
    # ==============================

    if not ciudad:
        errores.append("Debes seleccionar una ciudad.")

    # ==============================
    # VALIDAR GÉNERO
    # ==============================

    if not genero:
        errores.append("Debes seleccionar un género.")

    # ==============================
    # VALIDAR INTERESES
    # ==============================

    if not intereses:
        errores.append("Debes seleccionar al menos un interés.")

    # ==============================
    # SI HAY ERRORES
    # ==============================

    if errores:
        for error in errores:
            flash(error, "registro")

        return redirect("/")

    # ==============================
    # HASHEAR CONTRASEÑA
    # ==============================

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # ==============================
    # PREPARAR DATOS
    # ==============================

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password_hash,
        "fecha_nacimiento": fecha_nacimiento,
        "ciudad": ciudad,
        "genero": genero,
        "intereses": ", ".join(intereses)
    }

    # ==============================
    # GUARDAR USUARIO
    # ==============================

    usuario_id = Usuario.guardar(data)

    if not usuario_id:
        flash("Ocurrió un error al registrar el usuario.", "registro")
        return redirect("/")

    # ==============================
    # CREAR SESIÓN
    # ==============================

    session["usuario_id"] = usuario_id

    return redirect("/exito")


@usuarios_bp.route("/login", methods=["POST"])
def login():

    email = request.form["email"].strip()
    password = request.form["password"]

    usuario = Usuario.buscar_por_email(email)

    if not usuario:
        flash("El e-mail o la contraseña son incorrectos.", "login")
        return redirect("/")

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        usuario.password.encode("utf-8")
    ):
        flash("El e-mail o la contraseña son incorrectos.", "login")
        return redirect("/")

    session["usuario_id"] = usuario.id

    return redirect("/exito")


@usuarios_bp.route("/exito")
def exito():

    if "usuario_id" not in session:
        return redirect("/")

    usuario = Usuario.buscar_por_id(session["usuario_id"])

    if not usuario:
        session.clear()
        return redirect("/")

    return render_template("exito.html", usuario=usuario)


@usuarios_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")