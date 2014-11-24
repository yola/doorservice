from collections import OrderedDict

USERNAME = 'username'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = 5000

TIMED_DELAY = 2

BUTTONS = OrderedDict(
    {
        'Open Outer': {
            'pin': 0,
            'delay': 0.5,
        },
        'Open Inner': {
            'pin': 1,
            'delay': 1,
        },
    }
)
