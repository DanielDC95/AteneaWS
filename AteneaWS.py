from flask import Flask, jsonify
from flask import request
from db_connection import db_connection
import psycopg2
import json
from models import genres

app = Flask(__name__)

dbc = db_connection("user","password","localhost","5432","ateneadb")
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
        my_genre = genres("0","{}".format(request_json["name"]))
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

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)