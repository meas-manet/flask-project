import psycopg2
from psycopg2.extras import DictCursor,RealDictCursor
con=psycopg2.connect(dbname="python",
            user="postgres",
            password="dexter",
            host="localhost",
            port="5432")

class PgConfig:
    @staticmethod
    def getCursor():
        cur = con.cursor(cursor_factory=DictCursor)
        return cur

    @staticmethod
    def PgCommit():
        con.commit()
