from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Tarea:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.prioridad = data['prioridad']
        self.estado = data['estado']
        self.fecha_limite = data['fecha_limite']
        self.usuario_id = data['usuario_id']
        self.categoria_id = data['categoria_id']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.categoria_nombre = data.get('categoria_nombre')

    @classmethod
    def guardar(cls, data):
        query = """
                INSERT INTO tareas (titulo, descripcion, prioridad, estado, fecha_limite, usuario_id, categoria_id, created_at)
                VALUES (%(titulo)s, %(descripcion)s, %(prioridad)s, %(estado)s, %(fecha_limite)s, %(usuario_id)s, %(categoria_id)s, NOW());
                """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def obtener_por_usuario(cls, data):
        query = """
                SELECT tareas.*, categorias.nombre AS categoria_nombre 
                FROM tareas 
                JOIN categorias ON tareas.categoria_id = categorias.id 
                WHERE tareas.usuario_id = %(usuario_id)s
                ORDER BY tareas.fecha_limite ASC;
                """
        resultados = connectToMySQL().query_db(query, data)
        tareas = []
        if resultados:
            for fila in resultados:
                tareas.append(cls(fila))
        return tareas

    @classmethod
    def obtener_proximas_tareas(cls, data):
        query = """
                SELECT tareas.*, DATEDIFF(fecha_limite, CURDATE()) AS dias_restantes 
                FROM tareas 
                WHERE usuario_id = %(usuario_id)s AND estado != 'Completada'
                ORDER BY fecha_limite ASC LIMIT 5;
                """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def obtener_por_id(cls, data):
        query = """
                SELECT tareas.*, categorias.nombre AS categoria_nombre 
                FROM tareas 
                JOIN categorias ON tareas.categoria_id = categorias.id 
                WHERE tareas.id = %(id)s;
                """
        resultado = connectToMySQL().query_db(query, data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

    @classmethod
    def actualizar(cls, data):
        query = """
                UPDATE tareas 
                SET titulo = %(titulo)s, descripcion = %(descripcion)s, 
                    prioridad = %(prioridad)s, estado = %(estado)s, 
                    fecha_limite = %(fecha_limite)s, categoria_id = %(categoria_id)s
                WHERE id = %(id)s;
                """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def cambiar_estado(cls, data):
        query = "UPDATE tareas SET estado = %(estado)s WHERE id = %(id)s;"
        return connectToMySQL().query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM tareas WHERE id = %(id)s;"
        return connectToMySQL().query_db(query, data)

    @staticmethod
    def validar_tarea(data):
        is_valid = True
        if len(data['titulo'].strip()) < 3:
            flash("El título debe tener al menos 3 caracteres.", "tarea")
            is_valid = False
        if not data.get('categoria_id'):
            flash("Debe seleccionar una categoría.", "tarea")
            is_valid = False
        if not data.get('prioridad'):
            flash("Debe seleccionar una prioridad.", "tarea")
            is_valid = False
        if not data.get('fecha_limite'):
            flash("Debe ingresar una fecha límite.", "tarea")
            is_valid = False
        elif str(data['fecha_limite']) < str(datetime.now().date()):
            flash("La fecha límite no puede ser una fecha pasada.", "tarea")
            is_valid = False
        if len(data['descripcion'].strip()) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "tarea")
            is_valid = False
        return is_valid