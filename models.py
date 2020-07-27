from db_connection import db_connection
from flask import jsonify

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
        result = self.conn.insert_record("genres","idgenre",dic_genre)
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
        result = self.conn.insert_record("publishers","idpublisher",dic_publisher)
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
        result = self.conn.insert_record("authors","idauthor",dic_author)
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
        result = self.conn.insert_record("country","idcountry", dic_country)
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


class books:

    def __init__(self, id, isbn, title, list_authors, id_publisher, id_genre, published_date, description, price, image_path):
        self.id = id
        self.isbn = isbn
        self.title = title 
        self.list_authors = list_authors
        self.id_publisher = id_publisher
        self.id_genre = id_genre
        self.publiched_date = published_date
        self.description = description
        self.price = price
        self.image_path = image_path
    
    def add_book(self):
        msg = ""
        v_authors = self.verify_authors()
        v_publishers = self.verify_publishers()
        v_genres = self.verify_genres()
        dic_book = {'isbn': self.isbn, 'title': self.title, 'idpublisher': self.id_publisher, 'idgenre': self.id_genre, 'publisheddate': self.publiched_date, 'description': self.description, 'price': self.price, 'imagepath': self.image_path }

        if len(v_authors) > 0:
            authors = ""
            for i in range(len(v_authors)):
                if i == 0:
                    authors = "{}".format(v_authors[i])
                else:
                    authors += ", {}".format(v_authors[i])
                
            result = {"result": "Los siguientes id's de autores no existen: {}".format(authors)}
            return result   

        if len(v_publishers) > 0:
            publishers = ""
            for i in range(len(v_publishers)):
                if i == 0:
                    publishers = "{}".format(v_publishers[i])
                else:
                    publishers += ", {}".format(v_publishers[i])
                
            result = {"result": "Los siguientes id's de editoriales no existen: {}".format(publishers)}
            return result   
        
        if len(v_genres) > 0:
            genres = ""
            for i in range(len(v_genres)):
                if i == 0:
                    genres = "{}".format(v_genres[i])
                else:
                    genres += ", {}".format(v_genres[i])
                
            result = {"result": "Los siguientes id's de generos no existen: {}".format(genres)}
            return result   
        
        result = self.conn.insert_record("books","idbook", dic_book)
        self.id = result["idbook"]
        
        #if result=="Success":
        for i in range(len(self.list_authors)):
            dic_book_authors = eval(self.list_authors[i])
            dic_book_authors['idbook'] = "{}".format(self.id )
            result2 = self.conn.insert_record("bookauthors","id", dic_book_authors)

        return result2   

    def update_book(self):
        dic_book = {'isbn': self.isbn, 'title': self.title, 'idpublisher': self.id_publisher, 'idgenre': self.id_genre, 'publisheddate': self.publiched_date, 'description': self.description, 'price': self.price, 'imagepath': self.image_path }
        condition = "idbook = " + self.id
        result = self.conn.update_record("books", dic_book, condition)
        return result

    def delete_book(self):
        dic_book = {'idbook': self.id}
        result = self.conn.delete_record("books", dic_book)
        return result

    def get_dbconnection(self, dbc):
        self.conn = dbc

    def verify_authors(self):
        not_exits_list = []
        for i in (0, len(self.list_authors)-1):
            
            dic_author = eval(self.list_authors[i])

            for key in dic_author.keys():
                author_id = dic_author[key]
                query = "Select Count(name) from authors where idauthor = {};".format(author_id)
                cursor = self.conn.execute_query(query)
            

                for row in cursor:
                    count_result = row[0]

            if count_result == 0:
                not_exits_list.append(author_id)
        
        return not_exits_list

    def verify_publishers(self):
        not_exits_list = []
        query = "Select Count(name) from publishers where idpublisher = {};".format(self.id_publisher)
        cursor = self.conn.execute_query(query)

        for row in cursor:
            count_result = row[0]
        
        if count_result == 0:
                not_exits_list.append(self.id_publisher)

        return not_exits_list

    def verify_genres(self):
        not_exits_list = []
        query = "Select Count(name) from genres where idgenre = {};".format(self.id_genre)
        cursor = self.conn.execute_query(query)

        for row in cursor:
            count_result = row[0]
        
        if count_result == 0:
                not_exits_list.append(self.id_genre)

        return not_exits_list