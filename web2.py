import flask
from markupsafe import escape
import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        return '123'
    #elif flask.request.method == 'GET':
    #    return '456'

    return flask.render_template('index.html')

@app.route('/world')
def hello():
    return 'World'


@app.route('/date')
def get_date():
    return str(datetime.datetime.now().date())


@app.route('/user/<username>')
def get_user(username):
    return f'User {escape(username)}'
