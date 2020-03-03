from flask import Flask, jsonify
from flask import request
from db_connection import db_connection
import psycopg2
import json
from models import genres, publishers, authors, countrys

app = Flask(__name__)

dbc = db_connection("","","localhost","5432","ateneadb")
dbc.connect_to_db()

#Returns a genre list
@app.route("/get_genres", methods=['GET'])
def get_genres():
    if (request.method == 'GET'):
        query_result = []
        cursor_dic = {}
       
        cursor = dbc.execute_query("Select * From genres;")
        
        for row in cursor:
            cursor_dic = {}

            for col, description in enumerate(cursor.description):
                cursor_dic.update({description[0] : row[col]})
            
            query_result.append(cursor_dic)
        
        return jsonify(query_result)

#Add a new genre
@app.route("/add_genre", methods = ['POST'])
def add_genre():
    if request.method == 'POST':
        request_json = request.get_json()
        id = 0
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        print(name)
        my_genre = genres(id,name)
        my_genre.get_dbconnection(dbc)
        result = my_genre.add_genre()
        
        return jsonify({"about":"{}".format(result)})

#Update a genre
@app.route("/update_genre", methods = ['POST'])
def update_genre():
    if request.method == 'POST':
        request_json = request.get_json()
        my_genre = genres("{}".format(request_json["id"]),"{}".format(request_json["name"]))
        my_genre.get_dbconnection(dbc)
        result = my_genre.update_genre()
        return jsonify({"about":"{}".format(result)})

#Delete a genre
@app.route("/delete_genre", methods = ['POST'])
def delete_genre():
    if request.method == 'POST':
        request_json = request.get_json()
        my_genre = genres("{}".format(request_json["id"]),"{}".format(request_json["name"]))
        my_genre.get_dbconnection(dbc)
        result = my_genre.delete_genre()
        return jsonify({"about":"{}".format(result)})

#////////////////////////////////////////////////////////////////////////////////////////////////////////////77

#Returns a publisher list
@app.route("/get_publishers", methods=['GET'])
def get_publishers():
    if (request.method == 'GET'):
        query_result = []
        cursor_dic = {}
       
        cursor = dbc.execute_query("Select * From publishers;")
        
        for row in cursor:
            cursor_dic = {}

            for col, description in enumerate(cursor.description):
                cursor_dic.update({description[0] : row[col]})
            
            query_result.append(cursor_dic)
        
        return jsonify(query_result)

#Add a new publisher
@app.route("/add_publisher", methods = ['POST'])
def add_publisher():
    if request.method == 'POST':
        request_json = request.get_json()
        id = 0
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        my_publisher = publishers(id,name)
        my_publisher.get_dbconnection(dbc)
        result = my_publisher.add_publisher()
        
        return jsonify({"about":"{}".format(result)})

#Update a publisher
@app.route("/update_publisher", methods = ['POST'])
def update_publisher():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        my_publisher = publishers("{}".format(request_json["id"]),name)
        my_publisher.get_dbconnection(dbc)
        result = my_publisher.update_publisher()
        return jsonify({"about":"{}".format(result)})

#Delete a publisher
@app.route("/delete_publisher", methods = ['POST'])
def delete_publisher():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        my_publisher = publishers("{}".format(request_json["id"]),name)
        my_publisher.get_dbconnection(dbc)
        result = my_publisher.delete_publisher()
        return jsonify({"about":"{}".format(result)})

#////////////////////////////////////////////////////////////////////////////////////////////////////////////77

#Returns a author list
@app.route("/get_authors", methods=['GET'])
def get_authors():
    if (request.method == 'GET'):
        query_result = []
        cursor_dic = {}
       
        cursor = dbc.execute_query("Select * From authors;")
        
        for row in cursor:
            cursor_dic = {}

            for col, description in enumerate(cursor.description):
                cursor_dic.update({description[0] : row[col]})
            
            query_result.append(cursor_dic)
        
        return jsonify(query_result)

#Add a new author
@app.route("/add_author", methods = ['POST'])
def add_author():
    if request.method == 'POST':
        request_json = request.get_json()
        id = 0
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        last_name = "{}".format(request_json["last_name"])
        last_name = last_name.replace("'", "''")
        born_date = "{}".format(request_json["born_date"])
        born_date = born_date.replace("'", "''")
        id_country = "{}".format(request_json["id_country"])
        id_country = id_country.replace("-", "")
        my_author = authors(id,name,last_name,born_date,id_country)
        my_author.get_dbconnection(dbc)
        result = my_author.add_author()
        
        return jsonify({"about":"{}".format(result)})

#Update a author
@app.route("/update_author", methods = ['POST'])
def update_author():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        last_name = "{}".format(request_json["last_name"])
        last_name = last_name.replace("'", "''")
        born_date = "{}".format(request_json["born_date"])
        born_date = born_date.replace("'", "''")
        id_country = "{}".format(request_json["id_country"])
        id_country = id_country.replace("-", "")
        my_author = authors(id,name,last_name,born_date,id_country)
        my_author.get_dbconnection(dbc)
        result = my_author.update_author()
        return jsonify({"about":"{}".format(result)})

#Delete a author
@app.route("/delete_author", methods = ['POST'])
def delete_author():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        last_name = "{}".format(request_json["last_name"])
        last_name = last_name.replace("'", "''")
        born_date = "{}".format(request_json["born_date"])
        born_date = born_date.replace("'", "''")
        id_country = "{}".format(request_json["id_country"])
        id_country = id_country.replace("-", "")
        my_author = authors(id,name,last_name,born_date,id_country)
        my_author.get_dbconnection(dbc)
        result = my_author.delete_author()
        return jsonify({"about":"{}".format(result)})

################################Countrys
#Returns a country list
@app.route("/get_countrys", methods=['GET'])
def get_countrys():
    if (request.method == 'GET'):
        query_result = []
        cursor_dic = {}
       
        cursor = dbc.execute_query("Select * From country;")
        
        for row in cursor:
            cursor_dic = {}

            for col, description in enumerate(cursor.description):
                cursor_dic.update({description[0] : row[col]})
            
            query_result.append(cursor_dic)
        
        return jsonify(query_result)

#Add a new country
@app.route("/add_country", methods = ['POST'])
def add_country():
    if request.method == 'POST':
        request_json = request.get_json()
        id = 0
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        code = "{}".format(request_json["code"])
        my_country = countrys(id,code,name)
        my_country.get_dbconnection(dbc)
        result = my_country.add_country()
        
        return jsonify({"about":"{}".format(result)})

#Update a country
@app.route("/update_country", methods = ['POST'])
def update_country():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        code = "{}".format(request_json["code"])
        my_country = countrys("{}".format(request_json["id"]),code,name)
        my_country.get_dbconnection(dbc)
        result = my_country.update_country()
        return jsonify({"about":"{}".format(result)})

#Delete a country
@app.route("/delete_country", methods = ['POST'])
def delete_country():
    if request.method == 'POST':
        request_json = request.get_json()
        name = "{}".format(request_json["name"])
        name = name.replace("'", "''")
        code = "{}".format(request_json["code"])
        my_country = countrys("{}".format(request_json["id"]),code,name)
        my_country.get_dbconnection(dbc)
        result = my_country.delete_country()
        return jsonify({"about":"{}".format(result)})

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)