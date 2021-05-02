#!/usr/bin/python3
"""start Flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """main page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """str"""
    return "HBNB"


@app.route('/c/<phrase>', strict_slashes=False)
def c(phrase):
    """Print c phrases"""
    return 'C {}'.format(phrase.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<phrase>', strict_slashes=False)
def python(phrase='is cool'):
    """string and is cool"""
    return 'Python {}'.format(phrase.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)