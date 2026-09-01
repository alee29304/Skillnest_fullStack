# ==========================================================
# VISITAS - SESIONES EN FLASK
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)


# ==========================================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# SECRET KEY
# ==========================================================

app.secret_key = "clave-secreta"


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():

    # Si no existe el contador, lo creamos.
    if "visitas" not in session:
        session["visitas"] = 1

    else:
        # Si venimos de una acción, no sumamos otra visita.
        if session.get("accion", False):
            session["accion"] = False

        else:
            # Entrada o recarga normal de la página.
            session["visitas"] += 1


    # Inicializar contador de reinicios.
    if "reinicios" not in session:
        session["reinicios"] = 0


    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


# ==========================================================
# AUMENTAR VISITAS EN 2
# ==========================================================

@app.route("/sumar_dos")
def sumar_dos():

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += 2

    # Indicar que volvemos desde una acción.
    session["accion"] = True

    return redirect(url_for("index"))


# ==========================================================
# REINICIAR CONTADOR
# ==========================================================

@app.route("/reiniciar")
def reiniciar():

    if "reinicios" not in session:
        session["reinicios"] = 0

    session["reinicios"] += 1

    # Reiniciar a 0.
    session["visitas"] = 0

    # Evitar que el redirect sume 1.
    session["accion"] = True

    return redirect(url_for("index"))


# ==========================================================
# SUMAR UNA CANTIDAD PERSONALIZADA
# ==========================================================

@app.route("/sumar", methods=["POST"])
def sumar():

    cantidad = int(request.form["cantidad"])

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += cantidad

    # Indicar que volvemos desde una acción.
    session["accion"] = True

    return redirect(url_for("index"))


# ==========================================================
# DESTRUIR TODA LA SESIÓN
# ==========================================================

@app.route("/destruir_sesion")
def destruir_sesion():

    session.clear()

    return redirect(url_for("index"))


# ==========================================================
# EJECUTAR APLICACIÓN
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)