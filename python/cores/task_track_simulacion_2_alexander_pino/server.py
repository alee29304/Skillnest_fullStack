from flask_app import app

# Importamos los controladores para que Flask registre todas las rutas
from flask_app.controllers import usuarios_controllers, categorias_controllers, tareas_controllers

if __name__ == "__main__":
    app.run(debug=True)