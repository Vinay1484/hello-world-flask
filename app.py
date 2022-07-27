from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def news():
    data = request.json
    return data["lang"]

if __name__ == '__main__':
    app.run()
