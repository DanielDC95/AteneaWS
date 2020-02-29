from flask import Flask, jsonify
from flask import request
import psycopg2
import json

app = Flask(__name__)

conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

@app.route("/get_genres", methods=['GET'])
def get_genres():
    if (request.method == 'GET'):
        query_result = []
        cursor_dic = {}
        cursor.execute("Select * From genres;")
        #row = cursor.__next__()
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
        
        cursor.execute("Insert Into genres (name) Values ('{}');".format(request_json["name"]))
        conn.commit()
        return jsonify({"about":"Success"})

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)