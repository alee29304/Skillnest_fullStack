from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante


class Curso:
    """
    Representa un registro de la tabla cursos.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.estudiantes = []


    @classmethod
    def get_all(cls):
        """
        Obtiene todos los cursos.
        """

        query = """
            SELECT
                id,
                nombre,
                created_at,
                updated_at
            FROM cursos
            ORDER BY nombre;
        """


        resultados = connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query)


        cursos = []


        for curso in resultados:

            cursos.append(
                cls(curso)
            )


        return cursos


    @classmethod
    def save(cls, data):
        """
        Crea un nuevo curso.
        """

        query = """
            INSERT INTO cursos
            (
                nombre
            )
            VALUES
            (
                %(nombre)s
            );
        """


        return connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(
            query,
            data
        )


    @classmethod
    def get_curso_con_estudiantes(cls, curso_id):
        ""