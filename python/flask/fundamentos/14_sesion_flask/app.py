# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect, session


# ==========================================
# CREAR APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# CLAVE SECRETA
# ==========================================

# Flask utiliza esta clave para proteger
# la información asociada a la sesión.
#
# En proyectos reales NO debemos publicar
# esta clave en GitHub.

app.secret_key = "una-clave-secreta"


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de creación
    de usuario.
    """

    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    """
    Recibe los datos enviados mediante POST
    y los almacena en la sesión.
    """

    # --------------------------------------
    # Obtener datos del formulario
    # --------------------------------------

    nombre = request.form["nombre"]

    email = request.form["email"]


    # --------------------------------------
    # Mostrar información en la terminal
    # --------------------------------------

    print("===================================")

    print("Información recibida")

    print(f"Nombre: {nombre}")

    print(f"Email: {email}")

    print("===================================")


    # --------------------------------------
    # Guardar información en la sesión
    # --------------------------------------

    session["nombre_usuario"] = nombre

    session["email_usuario"] = email


    # --------------------------------------
    # Redireccionar
    # --------------------------------------

    return redirect("/mostrar_usuario")


# ==========================================
# MOSTRAR USUARIO
# ==========================================

@app.route("/mostrar_usuario")
def mostrar_usuario():
    """
    Recupera la información almacenada
    en la sesión.
    """

    # --------------------------------------
    # Leer información desde session
    # --------------------------------------

    nombre = session["nombre_usuario"]

    email = session["email_usuario"]

    ciudad = session["ciudad_usuario"]

    # --------------------------------------
    # Mostrar información en terminal
    # --------------------------------------

    print("===================================")

    print("Usuario redirigido")

    print(f"Nombre: {nombre}")

    print(f"Email: {email}")

    print(f"Ciudad: {ciudad}")

    print("===================================")


    # --------------------------------------
    # Renderizar plantilla
    # --------------------------------------

    return render_template("mostrar.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
