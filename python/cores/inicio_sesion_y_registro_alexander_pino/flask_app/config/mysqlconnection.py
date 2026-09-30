import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


class MySQLConnection:

    def __init__(self, db):
        self.db = db
        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data or ())

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                return cursor.lastrowid

            except Exception as e:
                print("Algo salió mal:", e)
                return False


def connectToMySQL(db):
    return MySQLConnection(db)