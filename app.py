from flask import Flask
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {}
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("create table if not exists views (views integer primary key autoincrement, time timestamp default current_timestamp)")
    cursor.execute("PRAGMA database_list")
    conn.commit()
    conn.close()
    return json.dumps(cursor.fetchall())

if __name__ == '__main__':
    app.run()
