#!/usr/bin/python3

"""Flask start"""
from flask import Flask


app = flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Hello"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
