from flask import Flask
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("create table if not exists views (views integer primary key autoincrement, time timestamp default current_timestamp)")
    cursor.execute("insert into views default values")
    cursor.execute("select count(*) from views")
    conn.commit()
    return json.dumps({views : cursor.fetchall()[0][0]})

if __name__ == '__main__':
    app.run()
