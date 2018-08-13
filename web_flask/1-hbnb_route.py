#!/usr/bin/python3
from flask import Flask
''' Basic flask application'''

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def holberton():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbhn():
    return 'HBNB'


app.run(host='0.0.0.0', port=5000)
