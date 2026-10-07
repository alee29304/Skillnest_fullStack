from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "5e9a3cd3f2224ab537d837622409822e"
bcrypt = Bcrypt(app)