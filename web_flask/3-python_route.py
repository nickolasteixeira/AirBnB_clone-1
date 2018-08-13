#!/usr/bin/python3
from flask import Flask
''' Basic Flask application'''

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def holberton():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

app.run(host='0.0.0.0', port=5000)
