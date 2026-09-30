import os
from flask import Flask
from dotenv import load_dotenv
from flask_app.controllers.usuarios import usuarios_bp

load_dotenv()

app = Flask(__name__, template_folder="flask_app/templates", static_folder="flask_app/static")

# Coincide con SECRET_KEY de tu .env
app.secret_key = os.getenv("SECRET_KEY", "clave_por_defecto")

app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=True)