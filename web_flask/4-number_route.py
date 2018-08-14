#!/usr/bin/python3
from flask import Flask
'''Basic Flask Application'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def holberton():
    '''display HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''display HBNB'''
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    '''C!'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    '''python is cool'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    '''number'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
