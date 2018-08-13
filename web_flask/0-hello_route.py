#!/usr/bin/python3
from flask import Flask
''' Basic flask application'''


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holberton():
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=int('5000'))
