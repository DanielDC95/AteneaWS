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


class publishers:

    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def get_name(self):
        return self.name

    def add_publisher(self):
        dic_publisher = {'name' : self.name}
        result = self.conn.insert_record("publishers",dic_publisher)
        return result

    def update_publisher(self):
        dic_publisher = {'name' : self.name}
        condition = "idpublisher = " + self.id
        result = self.conn.update_record("publishers",dic_publisher,condition)
        return result

    def delete_publisher(self):
        dic_publicher = {'idpublisher' : self.id}
        result = self.conn.delete_record("publisher",dic_publicher)
        return result

    def get_dbconnection(self, dbc):
        self.conn = dbc
        