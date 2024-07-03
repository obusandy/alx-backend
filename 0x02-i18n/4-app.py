#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    """
    A config class for the flask app
    Config class that has a LANGUAGES class attribute
    Holds configurations for languages and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize the Flask app
app = Flask(__name__)
# Load configurations
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    force a particular locale by passing
    the locale=fr parameter to your app URLs.
    returns the best supported language
    """
    usrlang = request.args.get('locale')
    if usrlang and usrlang in app.config['LANGUAGES']:
        return usrlang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template
    display level 1 heading
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
