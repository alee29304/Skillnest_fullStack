from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "clave-secreta"


@app.route("/")
def index():

    if "visitas" in session:
        session["visitas"] += 1
    else:
        session["visitas"] = 1

    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")


@app.route("/sumar_dos")
def sumar_dos():
    session["visitas"] += 2
    return redirect("/")


@app.route("/reiniciar")
def reiniciar():
    session["visitas"] = 0
    session["reinicios"] += 1
    return redirect("/")


@app.route("/sumar", methods=["POST"])
def sumar():
    numero = int(request.form["numero"])
    session["visitas"] += numero
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)