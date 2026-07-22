from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "<h1>🌎 ¡Bienvenido a nuestro servidor Flask!</h1>"

# Ruta genérica para explorar enrutamiento
@app.route("/explorar")
def explorar():
    return "<h1>🔍 ¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!</h1>"

# Rutas dinámicas para personalización
@app.route("/perfil/<nombre>")
def personalizar(nombre):
    return f"<h1>👤 Bienvenid@ {nombre} a tu perfil personalizado en nuestra app.</h1>"

# Ruta que repite un mensaje varias veces
@app.route("/repetir/<int:veces>/<mensaje>")
def repetir(mensaje, veces):
    return f"<h1>🔄 Repite después de mí: {' '.join([mensaje] * veces)} </h1>"

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.route("/error")
def error():
    return "<h1>⚠️ ¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo.</h1>"

# Ejecuta el servidor
if __name__ == "__main__":
   app.run(debug=True)