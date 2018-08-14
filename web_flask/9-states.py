#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models import State
from os import getenv
'''Basic Flask Application'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states_list')
def states_list():
    '''list all states'''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage.all(State).values()
    else:
        states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    ''' lists all ids associated with id'''
    if getenv('HBNB-TYPE_STORAGE') == 'db':
        states = storage.all(State)
    else:
        states = storage.all(State)

    key = "State.{}".format(id)
    if key in states:
        state = states[key]
    else:
        state = None

    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    '''tear down app'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
