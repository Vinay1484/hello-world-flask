from flask import Flask
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("create table if not exists userss (id integer primary key autoincrement, name text, password text)")
    cursor.execute("insert into userss(name,password) values('admin','admin')")
    cursor.execute("select * from userss")
    conn.commit()
    return json.dumps(cursor.fetchall())

if __name__ == '__main__':
    app.run()
