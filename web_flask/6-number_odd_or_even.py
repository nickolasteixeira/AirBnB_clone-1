#!/usr/bin/python3
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    '''number template'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    '''odd or even'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
