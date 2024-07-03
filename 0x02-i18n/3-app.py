#!/usr/bin/env python3
"""
Setup a basic Flask app with Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    """
    Config class
    that has a LANGUAGES class attribute
    Holds configurations for languages and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC' # time zone.


# Initialize the Flask app

app = Flask(__name__)
# Load configurations
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Uses the 'Accept-Language' header from the request
    to select the most appropriate language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
