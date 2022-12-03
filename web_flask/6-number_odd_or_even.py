#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask
from flask import render_template


APP = Flask(__name__)
APP.jinja_env.trim_blocks = True
APP.jinja_env.lstrip_blocks = True


@APP.route("/", strict_slashes=False)
def hello_holberton():
    """
    Returns 'Hello HBNB!'.
    """
    return "Hello HBNB!"

@APP.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB'.
    """
    return "HBNB"

@APP.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """
    Returns C, followed by text value.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@APP.route("/python", strict_slashes=False)
@APP.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """
    Returns Python, followed by text value.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@APP.route("/number/<int:n>", strict_slashes=False)
def IsINT(n):
    """
    Returns n is a number if n is a integer.
    """
    return "{} is a number".format(n)

@APP.route("/number_template/<int:n>", strict_slashes=False)
def nTemp(n):
    """
    Displays a HTML page if n is an integer.
    """
    return render_template("5-number.html", n=n)

@APP.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def OddOrEven(n):
    """
    Displays an HTML page if n is an integer.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port="5000")
