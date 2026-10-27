from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def guardar(cls, data):
        query = """
                INSERT INTO usuarios (nombre, apellido, email, password, created_at) 
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW());
                """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def obtener_por_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL().query_db(query, data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

    @classmethod
    def obtener_por_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL().query_db(query, data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

    @staticmethod
    def validar_registro(data):
        is_valid = True
        if len(data['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            is_valid = False
        if len(data['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("El email no tiene un formato válido.", "registro")
            is_valid = False
        if Usuario.obtener_por_email({'email': data['email']}):
            flash("El email ya se encuentra registrado.", "registro")
            is_valid = False
        if len(data['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            is_valid = False
        if data['password'] != data['confirmar_password']:
            flash("Las contraseñas no coinciden.", "registro")
            is_valid = False
        return is_valid