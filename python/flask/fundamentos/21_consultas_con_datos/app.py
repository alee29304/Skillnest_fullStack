# ==========================================================
# SERVIDOR FLASK
# ==========================================================

from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """

    mascotas = Mascota.get_all()

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR ID
# ==========================================================

@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca la mascota
    correspondiente en la base de datos.
    """

    mascota = Mascota.get_by_id(id)


    # ------------------------------------------------------
    # Si no existe la mascota, mostramos un mensaje.
    # ------------------------------------------------------

    if mascota is None:

        return "Mascota no encontrada", 404


    # ------------------------------------------------------
    # Mostrar mascota encontrada.
    # ------------------------------------------------------

    return render_template(
        "mascota.html",
        mascota=mascota
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
