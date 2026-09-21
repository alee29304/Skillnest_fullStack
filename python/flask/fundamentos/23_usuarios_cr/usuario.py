# ==========================================================
# MODELO USUARIO
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE USUARIO
# ==========================================================

class Usuario:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en un objeto Usuario.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.apellido = data["apellido"]

        self.email = data["email"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    # ======================================================
    # READ
    # OBTENER TODOS LOS USUARIOS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Recupera todos los usuarios de la base de datos.

        Retorna una lista de objetos Usuario.
        """

        # --------------------------------------------------
        # CONSULTA
        # --------------------------------------------------

        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id;
        """


        # --------------------------------------------------
        # EJECUTAR CONSULTA
        # --------------------------------------------------

        resultados = connectToMySQL(
            "esquema_usuarios"
        ).query_db(query)


        # --------------------------------------------------
        # CREAR LISTA DE OBJETOS
        # --------------------------------------------------

        usuarios = []


        # --------------------------------------------------
        # CONVERTIR CADA DICCIONARIO
        # EN UN OBJETO Usuario
        # --------------------------------------------------

        for usuario in resultados:

            usuarios.append(
                cls(usuario)
            )


        # --------------------------------------------------
        # RETORNAR RESULTADOS
        # --------------------------------------------------

        return usuarios


    # ======================================================
    # CREATE
    # CREAR NUEVO USUARIO
    # ======================================================

    @classmethod
    def save(cls, data):
        """
        Inserta un nuevo usuario en la base de datos.

        Recibe un diccionario con:

        nombre
        apellido
        email
        """

        # --------------------------------------------------
        # INSERT
        # --------------------------------------------------
        #
        # Los datos provenientes del formulario NO se
        # concatenan directamente en el SQL.
        #
        # Utilizamos parámetros preparados.
        #
        # created_at y updated_at se generan mediante NOW().
        # --------------------------------------------------

        query = """
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s,
                NOW(),
                NOW()
            );
        """


        # --------------------------------------------------
        # EJECUTAR INSERT
        # --------------------------------------------------

        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )
