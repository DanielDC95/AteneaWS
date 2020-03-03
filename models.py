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

    def __init__(self, id, name, last_name, born_date, id_country):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.born_date = born_date
        self.id_country = id_country
    
    def add_author(self):
        dic_author = {'name' : self.name, 'lastname' : self.last_name, 'borndate' : self.born_date, 'idcountry' : self.id_country}
        result = self.conn.insert_record("authors",dic_author)
        return result

    def update_author(self):
        dic_author = {'name' : self.name, 'lastname' : self.last_name, 'borndate' : self.born_date, 'idcountry' : self.id_country}
        condition = "idauthor = " + self.id
        result = self.conn.update_record("authors", dic_author, condition)
        return result

    def delete_author(self):
        dic_author = {'idauthor' : self.id}
        result = self.conn.delete_record("authors",dic_author)
        return result
    
    def get_dbconnection(self, dbc):
        self.conn = dbc


class countrys:

    def __init__(self, id, code, name):
        self.id = id
        self.code = code 
        self.name = name 
    
    def add_country(self):
        dic_country = {'code': self.code,'name' : self.name}
        result = self.conn.insert_record("country", dic_country)
        return result

    def update_country(self):
        dic_country = {'code': self.code,'name' : self.name}
        condition = "idcountry = " + self.id
        result = self.conn.update_record("country", dic_country, condition)
        return result

    def delete_country(self):
        dic_country = {'idcountry' :  self.id}
        result = self.conn.delete_record("country", dic_country)
        return result

    def get_dbconnection(self, dbc):
        self.conn = dbc