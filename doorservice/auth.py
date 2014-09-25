from functools import wraps

from flask import request, Response, render_template
from doorservice import app

from settings import INNER_DOOR_LABEL, OUTER_DOOR_LABEL


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return (username == app.config['USERNAME'] and
            password == app.config['PASSWORD'])


def authenticate():
    """Sends a 401 response that enables basic auth"""
    context = {
        'auth': False,
        'outer_door': {
            'label': OUTER_DOOR_LABEL,
        },
        'inner_door': {
            'label': INNER_DOOR_LABEL,
        },
    }
    return Response(render_template('index.html', **context), 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def auth_decorator():
    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not check_auth(auth.username, auth.password):
                return authenticate()
            return f(*args, **kwargs)
        return decorated
    return requires_auth
