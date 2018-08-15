#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models import State
from os import getenv
'''Basic Flask Application'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''list all states'''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_list():
    '''list all states and cities'''
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''tear down app'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
