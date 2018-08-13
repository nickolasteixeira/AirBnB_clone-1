#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
from models import State
'''Basic Flask Applicatoin'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''list all states'''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''tear down app'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
