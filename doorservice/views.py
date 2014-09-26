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

    if request.form.get('outer-door-button') == 'open-door':
        outer_door['set'] = True
        outer_door['success'] = open_door(OUTER_DOOR_PIN, OUTER_DOOR_DELAY)
    elif request.form.get('inner-door-button') == 'open-door':
        inner_door['set'] = True
        inner_door['success'] = open_door(INNER_DOOR_PIN, INNER_DOOR_DELAY)

    return render_template('index.html', **context)


@app.errorhandler(404)
@auth_decorator()
def not_found(error):
    context = dict()
    context['auth'] = True

    return render_template('index.html', **context)


@app.context_processor
def inject_button_labels():
    return {
        'buttons': BUTTONS,
    }
