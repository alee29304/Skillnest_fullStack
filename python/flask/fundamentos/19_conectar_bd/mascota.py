# ==========================================================
# MODELO MASCOTA
# ==========================================================
#
# Este archivo representa la tabla "mascotas"
# mediante una clase de Python.
#
# ==========================================================


# Importamos la función encargada de crear
# una conexión con MySQL.

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus datos en atributos del objeto.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas almacenadas
        en la base de datos.

        Retorna una lista de objetos Mascota.
        """

        # --------------------------------------------------
        # Consulta SQL
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas;
        """


        # --------------------------------------------------
        # Ejecutar consulta
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        # --------------------------------------------------
        # Crear lista de objetos
        # --------------------------------------------------

        mascotas = []


        # --------------------------------------------------
        # Convertir cada diccionario en Mascota
        # --------------------------------------------------

        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        # --------------------------------------------------
        # Retornar resultado
        # --------------------------------------------------

        return mascotas