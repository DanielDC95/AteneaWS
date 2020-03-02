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
    

class authors:

    def __init__(self, id, name, last_name, born_date):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.born_date = born_date
    
    def add_author(self):
        dic_author = {'name' : self.name, 'lastname' : self.last_name, 'borndate' : self.born_date}
        result = self.conn.insert_record("authors",dic_author)
        return result

    def update_author(self):
        dic_author = {'name' : self.name, 'lastname' : self.last_name, 'borndate' : self.born_date}
        condition = "iduthor = " + self.id
        result = self.conn.update_record("authors", dic_author, condition)
        return result

    def delete_authors(self):
        dic_author = {'idauthor' : self.id}
        result = self.conn.delete_record("authors",dic_author)
        return result
    
    def get_dbconnection(self, dbc):
        self.conn = dbc
