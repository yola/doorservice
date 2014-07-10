from flask import render_template, make_response, jsonify
from doorservice import app
from auth import auth_decorator


@app.route("/")
@auth_decorator()
def index():
    context = {
        'title': 'Doorservice',
        'content': 'Hello World',
    }
    return render_template('index.html', **context)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)