from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Categoria:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.usuario_id = data['usuario_id']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.cantidad_tareas = data.get('cantidad_tareas', 0)

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO categorias (nombre, usuario_id, created_at) VALUES (%(nombre)s, %(usuario_id)s, NOW());"
        return connectToMySQL().query_db(query, data)

    @classmethod
    def obtener_por_usuario(cls, data):
        query = """
                SELECT categorias.*, COUNT(tareas.id) AS cantidad_tareas 
                FROM categorias 
                LEFT JOIN tareas ON categorias.id = tareas.categoria_id 
                WHERE categorias.usuario_id = %(usuario_id)s 
                GROUP BY categorias.id;
                """
        resultados = connectToMySQL().query_db(query, data)
        categorias = []
        if resultados:
            for fila in resultados:
                categorias.append(cls(fila))
        return categorias

    @classmethod
    def obtener_por_id(cls, data):
        query = "SELECT * FROM categorias WHERE id = %(id)s;"
        resultado = connectToMySQL().query_db(query, data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM categorias WHERE id = %(id)s;"
        return connectToMySQL().query_db(query, data)

    @staticmethod
    def validar_categoria(data):
        is_valid = True
        if len(data['nombre'].strip()) < 3:
            flash("El nombre de la categoría debe tener al menos 3 caracteres.", "categoria")
            is_valid = False
        return is_valid