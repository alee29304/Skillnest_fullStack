import re
from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.fecha_nacimiento = data["fecha_nacimiento"]
        self.ciudad = data["ciudad"]
        self.genero = data["genero"]
        self.intereses = data["intereses"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO usuarios
            (nombre, apellido, email, password, fecha_nacimiento, ciudad, genero, intereses)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s, %(ciudad)s, %(genero)s, %(intereses)s);
        """
        return connectToMySQL("login_registro").query_db(query, data)

    @classmethod
    def buscar_por_email(cls, email):
        query = """
            SELECT *
            FROM usuarios
            WHERE email = %(email)s;
        """
        data = {
            "email": email
        }

        resultado = connectToMySQL("login_registro").query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None

    @classmethod
    def buscar_por_id(cls, id):
        query = """
            SELECT *
            FROM usuarios
            WHERE id = %(id)s;
        """
        data = {
            "id": id
        }

        resultado = connectToMySQL("login_registro").query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None