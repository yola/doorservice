from flask import render_template, request
from doorservice import app
from auth import auth_decorator

from open_door import open_door
from settings import (INNER_DOOR_LABEL, INNER_DOOR_PIN, INNER_DOOR_DELAY,
                      OUTER_DOOR_LABEL, OUTER_DOOR_PIN, OUTER_DOOR_DELAY)


@app.route("/", methods=['GET'])
@auth_decorator()
def index():
    context = dict()
    outer_door = dict()
    inner_door = dict()
    context['auth'] = True

    outer_door['label'] = OUTER_DOOR_LABEL
    inner_door['label'] = INNER_DOOR_LABEL

    context['outer_door'] = outer_door
    context['inner_door'] = inner_door
    return render_template('index.html', **context)


@app.route("/", methods=['POST'])
@auth_decorator()
def opendoor():
    context = dict()
    outer_door = dict()
    inner_door = dict()
    context['auth'] = True

    if request.form.get('outer-door-button') == 'open-door':
        outer_door['set'] = True
        outer_door['success'] = open_door(OUTER_DOOR_PIN, OUTER_DOOR_DELAY)
    elif request.form.get('inner-door-button') == 'open-door':
        inner_door['set'] = True
        inner_door['success'] = open_door(INNER_DOOR_PIN, INNER_DOOR_DELAY)

    outer_door['label'] = OUTER_DOOR_LABEL
    inner_door['label'] = INNER_DOOR_LABEL

    context['outer_door'] = outer_door
    context['inner_door'] = inner_door
    return render_template('index.html', **context)


@app.errorhandler(404)
@auth_decorator()
def not_found(error):
    context = dict()
    outer_door = dict()
    inner_door = dict()
    context['auth'] = True

    outer_door['label'] = OUTER_DOOR_LABEL
    inner_door['label'] = INNER_DOOR_LABEL

    context['outer_door'] = outer_door
    context['inner_door'] = inner_door
    return render_template('index.html', **context)


@app.context_processor
def inject_button_labels():
    return {
        'outer_door_label': OUTER_DOOR_LABEL,
        'inner_door_label': INNER_DOOR_LABEL,
    }
