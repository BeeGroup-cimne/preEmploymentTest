

from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "api working"

@app.route("/consumption/", methods=['GET'])
def get_consumption():
    if request.method == 'GET':
        try:
            payload = request.args
            if "date" in payload:
                date = payload['date']

                query_date = "{} {}".format(date,'00:00:00')
                con = sqlite3.connect("test_db.sqlite")
                cur = con.cursor()
                query = 'SELECT * FROM consumption WHERE "index"="{}"'.format(query_date)
                value = cur.execute(query).fetchone()
                con.close()
                if value:
                    return {date:str(value[1])}
                else:
                    return {date: "No data"}
            return "Missing item 'date'"
        except Exception as e:
            return e

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')