from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡Hola Mundo!</h1>"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/saludo/<nombre>")
def saludo(nombre):

    return f"¡Hola {nombre}!"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):

    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces

@app.route("/despedida/<nombre>")
def despedida(nombre):

    return f"¡Hasta luego {nombre}!, ¡Esperamos verte pronto!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):

    return f"¡Hola {nombre}, tienes {edad} años.!"

@app.route("/suma/<int:a>/<int:b>")
def sumar(a, b):

    return f"La suma es {a + b}"

@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):

    return f"La multiplicación es {a * b}"

@app.route("/paridad/<int:numero>")
def paridad(numero):

    return f"El número {numero} es par"

if __name__ == "__main__":
    app.run(debug=True)