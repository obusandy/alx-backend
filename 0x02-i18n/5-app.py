#!/usr/bin/env python3
"""
Setup a basic Flask app with Babel
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Load configurations
class Config(object):
    """
    Configuration class
    that has a LANGUAGES class attribute
    Holds configurations for languages and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for language localization.
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Returns a user dict if a valid user is found
    """
    usr_id = request.args.get('login_as')

    if usr_id:
        try:
            return users.get(int(usr_id))
        except Exception:
            return None
    return None


@app.before_request
def before_request() -> None:
    """Adds a user to the global session before any other function
    is executed
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Returns the lang specified in query param 'locale' if valid
    """
    userlang = request.args.get('locale')
    if userlang and userlang in app.config['LANGUAGES']:
        return userlang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template
    display level 1 heading
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
