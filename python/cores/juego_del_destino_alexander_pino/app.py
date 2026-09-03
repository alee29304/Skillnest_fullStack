from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# La clave secreta es necesaria para que Flask pueda encriptar la sesión (session)
app.secret_key = "clave_secreta_destino_magico"

# Lista de predicciones posibles (mezcla de mensajes positivos y de advertencia/mala suerte)
PREDICCIONES = [
    # Mensajes positivos
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un gran éxito académico o profesional tocará a tu puerta antes de lo que te imaginas.",
    "Un viaje inesperado te abrirá la mente y te brindará momentos de absoluta felicidad.",
    "Recibirás una grata sorpresa económica que te dará mucha tranquilidad.",
    # Mensajes de mala suerte / advertencias
    "Cuidado con las decisiones impulsivas; podrías derramar tu café en tu camiseta favorita.",
    "Alguien cercano te pedirá prestado algo que tardará varias semanas en devolverte.",
    "Tus planes para el fin de semana se verán interrumpidos por una lluvia inesperada.",
    "Evita confiarte demasiado hoy: revisa dos veces antes de enviar un correo importante."
]

@app.route('/')
def index():
    """
    Ruta Principal (GET):
    Muestra el formulario para que el usuario ingrese sus datos.
    """
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    """
    Ruta para procesar el formulario (POST):
    1. Lee los datos enviados por el usuario mediante request.form.
    2. Los almacena en el diccionario 'session' de Flask.
    3. Genera una predicción y número de la suerte aleatorios.
    4. Redirige a la ruta '/futuro'.
    """
    # Guardamos los datos recibidos del formulario en la sesión
    session['nombre'] = request.form.get('nombre')
    session['edad'] = request.form.get('edad')
    session['color'] = request.form.get('color')
    session['animal'] = request.form.get('animal')
    
    # Seleccionamos aleatoriamente un mensaje de la lista de predicciones
    session['prediccion'] = random.choice(PREDICCIONES)
    
    # Generamos un número aleatorio de la suerte entre 1 y 100
    session['numero_suerte'] = random.randint(1, 100)

    # Aplicamos el patrón POST -> REDIRECT -> GET para evitar reenvíos al actualizar la página
    return redirect(url_for('futuro'))


@app.route('/futuro')
def futuro():
    """
    Ruta de Resultados (GET):
    Obtiene los datos guardados en 'session' y se los pasa a futuro.html para mostrarlos.
    """
    # Si la persona intenta entrar directo a /futuro sin llenar el formulario, la devolvemos al inicio
    if 'nombre' not in session:
        return redirect(url_for('index'))

    return render_template(
        'futuro.html',
        nombre=session.get('nombre'),
        edad=session.get('edad'),
        color=session.get('color'),
        animal=session.get('animal'),
        prediccion=session.get('prediccion'),
        numero_suerte=session.get('numero_suerte')
    )


if __name__ == '__main__':
    # Ejecuta el servidor en modo desarrollo
    app.run(debug=True)