from flask import Flask, jsonify
from flask import request
from db_connection import db_connection
import psycopg2
import json

app = Flask(__name__)

dbc = db_connection("","","localhost","5432","")
dbc.connect_to_db()

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


@app.route("/add_genre", methods = ['POST'])
def add_genre():
    if request.method == 'POST':
        request_json = request.get_json()
        
        cursor = dbc.execute_query("Insert Into genres (name) Values ('{}');".format(request_json["name"]))
        #conn.commit()
        return jsonify({"about":"Success"})

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)