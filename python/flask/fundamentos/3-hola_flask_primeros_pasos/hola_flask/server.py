from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola chat!"

@app.route("/nosotros")
def nosotros():
    return "Conócenos un poco más!"

@app.route("/contactos")
def contactos():
    return "Contáctanos!"

@app.route("/detalles")
def detalles():
    return "<h1>Conoce nuestros detalles!</h1>"

if __name__ == "__main__":
    app.run(debug=True)