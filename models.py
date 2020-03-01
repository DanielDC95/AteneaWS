from db_connection import db_connection

class genres:

    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def get_name(self):
        return self.name

    def update_genre(self):
        dic_genre = {'name': self.name}
        condition = "idgenre = " + self.id
        result = self.conn.update_record("genres",dic_genre,condition)
        return result
    
    def add_genre(self):
        dic_genre = {'name': self.name}
        result = self.conn.insert_record("genres",dic_genre)
        return result

    def delete_genre(self):
        dic_genre = {'idgenre': self.id}
        result = self.conn.delete_record("genres",dic_genre)
        return result

    def get_dbconnection(self,dbc):
        self.conn = dbc
