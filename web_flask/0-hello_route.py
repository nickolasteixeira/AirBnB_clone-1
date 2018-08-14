#!/usr/bin/python3
from flask import Flask
''' Basic flask application'''


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holberton():
    ''' Hi holberton'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
