import psycopg2

class db_connection:

    def __init__(self, db_user, db_password, db_host, db_port, db_database):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_database = db_database

    def connect_to_db(self):
        connection = psycopg2.connect(user = self.db_user, password = self.db_password, host = self.db_host, port = self.db_port, database = self.db_database)
        cursor = connection.cursor()
        self.cursor = cursor

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor