#!/usr/bin/python3
"""start Flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """main page"""
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """str"""
    return "HBNB"


@app.route('/c/<phrase>', methods=["GET"], strict_slashes=False)
def c(phrase):
    """Print c phrases"""
    return 'C {}'.format(phrase.replace('_', ' '))


@app.route('/python/', methods=["GET"], strict_slashes=False)
@app.route('/python/<phrase>', methods=["GET"], strict_slashes=False)
def python(phrase='is cool'):
    """string and is cool"""
    return 'Python {}'.format(phrase.replace('_', ' '))


@app.route("/number/<int:num>", methods=["GET"], strict_slashes=False)
def number(num):
    """is a number?"""
    if type(num) == int:
        return ("{} is a number".format(num))

@app.route("/number_template/<int:num>", methods=["GET"], strict_slashes=False)
def html(num):
    """page html"""
    if type(num) == int:
        return render_template('5-number.html', n=num)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
