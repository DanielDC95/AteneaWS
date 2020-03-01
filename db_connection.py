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

    def update_record(self, table, dic, condition):
        fields = ""
        first = True
        result = ""
        try:
            for key in dic.keys():
                if first == True:
                    fields = key + " = '" + dic[key] + "'"
                    first = False
                else: 
                    fields += ", " + key + " = '" + dic[key] + "'"
                
            query_update = "Update {} Set {} Where {};".format(table,fields,condition)
            #print(query_update)
            self.cursor.execute(query_update)
            result = "Success"
        except:
            result = "Failure"
        return result

    def insert_record(self, table, dic):
        fields = ""
        values = ""
        first = True
        result = ""

        try:
            for key in dic.keys():
                if first == True:
                    fields = key
                    values = "'" + dic[key] + "'"
                    first = False
                else:
                    fields += ", " + key
                    values += ", '" + dic[key] + "'"
            
            query_insert = "Insert Into {} ({}) Values ({});".format(table,fields,values)
            self.cursor.execute(query_insert)
            #print(query_insert)
            result = "Success"
        except:
            result = "Failure"
        
        return result

