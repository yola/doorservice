from flask import render_template, request
from doorservice import app
from auth import auth_decorator

from open_door import open_door


@app.route("/", methods=['GET'])
@auth_decorator()
def index():
    context = {
        'unset': True,
        'auth': True,
    }
    return render_template('index.html', **context)


@app.route("/", methods=['POST'])
@auth_decorator()
def opendoor():
    context = dict()

    context['success'] = False
    context['auth'] = True

    if request.form.get('door-button') == 'open-door':
        context['success'] = open_door()

    return render_template('index.html', **context)


@app.errorhandler(404)
@auth_decorator()
def not_found(error):
    context = {
        'auth': True,
        'success': False,
    }
    return render_template('index.html', **context)
