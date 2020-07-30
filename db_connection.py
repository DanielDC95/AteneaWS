import psycopg2
import sys

class db_connection:

    def __init__(self, db_user, db_password, db_host, db_port, db_database):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_database = db_database

    def connect_to_db(self):
        connection = psycopg2.connect(user = self.db_user, password = self.db_password, host = self.db_host, port = self.db_port, database = self.db_database)
        #cursor = connection.cursor()
        self.connection = connection

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except :
            #result = "Failure"
            print("Unexpected error:", sys.exc_info()[0])
        return cursor

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
            print(query_update)
            cursor = self.connection.cursor()
            cursor.execute(query_update)
            self.connection.commit()
            result_dic = {"result": "Success", "message": "Ok"}
        except :
            result_dic = {"result": "Failure", "message": "Error {} occurred.".format(sys.exc_info()[0])}
        
        return result_dic

    def insert_record(self, table, table_id, dic):
        fields = ""
        values = ""
        first = True
        result = ""
        query_condition = ""
        query_result = []

        try:

            #Orders the fields and values to insert
            for key in dic.keys():
                print(key)
                if first == True:
                    fields = key
                    values = "'" + dic[key] + "'"
                    query_condition = key + " = '" + dic[key] + "'"
                    first = False
                else:
                    fields += ", " + key
                    values += ", '" + dic[key] + "'"
                    query_condition += " And " + key + " = '" + dic[key] + "'"
            
            query_insert = "Insert Into {} ({}) Values ({});".format(table,fields,values)
            print(query_insert)
            
            cursor = self.connection.cursor()
            cursor.execute(query_insert)
            self.connection.commit()

            query_select = "Select {} From {} Where {};".format(table_id,table,query_condition)
            print(query_select)
            cursor.execute(query_select)
            self.connection.commit()

            for row in cursor:
                result_dic = {"result": "Success", "message": "Ok"}

                for col, description in enumerate(cursor.description):
                    result_dic.update({description[0] : row[col]})
                
        except :
            result_dic = {"result": "Failure"}
            
        return result_dic

    def delete_record(self, table, conditionDic):
        result = ""
        where_string = ""
        first = True
        try:
            for key in conditionDic.keys():
                if first == True:
                    where_string = key + " = " + conditionDic[key]
                    first = False
                else:
                    where_string += " And " + key + " = " + conditionDic[key]
            query_delete = "Delete From {} Where {};".format(table,where_string)
            print(query_delete)
            cursor = self.connection.cursor()
            cursor.execute(query_delete)
            self.connection.commit()
            result = "Success"
        except:
            result = "Failure"
        
        return result


