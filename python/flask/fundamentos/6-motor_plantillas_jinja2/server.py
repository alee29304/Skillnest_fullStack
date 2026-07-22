from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    return render_template("index.html",
     nombre = "Ale", 
     curso = "Desarrollo Web Flask",
     ciudad = "Santiago",
     anio = "2026",
     profesor=False,
     tecnologias=[
        "Python",
        "Flask",
        "HTML",
        "CSS"
        ])


@app.route("/videojuego")
def videojuego():

    return render_template("jugador.html",
       jugador="atk.",
       puntaje=9200,
       lider=True
       )

if __name__ == "__main__":

    app.run(debug=True)