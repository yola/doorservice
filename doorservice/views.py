from flask import render_template, request
from doorservice import app
from auth import auth_decorator

from open_door import open_door


@app.route("/", methods=['GET'])
@auth_decorator()
def index():
    context = dict()
    outer_door = dict()
    inner_door = dict()
    context['auth'] = True

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
        outer_door['success'] = open_door(0, 0.5)
    elif request.form.get('inner-door-button') == 'open-door':
        inner_door['set'] = True
        inner_door['success'] = open_door(1, 3)

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

    context['outer_door'] = outer_door
    context['inner_door'] = inner_door
    return render_template('index.html', **context)
