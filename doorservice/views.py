from flask import render_template, request
from doorservice import app
from auth import auth_decorator

from open_door import open_door
from settings import BUTTONS


@app.route("/", methods=['GET'])
@auth_decorator()
def index():
    context = dict()
    context['auth'] = True

    return render_template('index.html', **context)


@app.route("/", methods=['POST'])
@auth_decorator()
def opendoor():
    context = dict()
    context['auth'] = True
    button_pressed = ''
    for data in request.form:
        if data in BUTTONS:
            open_door(BUTTONS[data]['pin'], BUTTONS[data]['delay'])
            button_pressed = data

    context['button_pressed'] = button_pressed
    return render_template('index.html', **context)


@app.errorhandler(404)
@auth_decorator()
def not_found(error):
    context = dict()
    context['auth'] = True

    return render_template('index.html', **context)


@app.errorhandler(500)
@auth_decorator()
def internal_server_error(error):
    context = dict()
    context['auth'] = True
    context['state'] = 'danger'

    return render_template('index.html', **context)


@app.context_processor
def inject_button_labels():
    return {
        'buttons': BUTTONS,
    }
