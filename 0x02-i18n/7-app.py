#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict, Union
import pytz

# Sample users dictionary with user information

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    instantiate the Babel object in your app
    create a Config class that has a LANGUAGES
    class attr: equal to ["en", "fr"].
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Returns a user dict if a valid user is found,
    otherwise None.
    """
    usr = request.args.get('login_as')

    if usr:
        try:
            return users.get(int(usr))
        except Exception:
            return None
    return None


@app.before_request
def before_request() -> None:
    """
    dds a user to the global sess
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Returns the language specified in query parameter 'locale' if valid
    """
    usrlang = request.args.get('locale')
    if usrlang in app.config['LANGUAGES']:
        return usrlang

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_lcl = request.headers.get('locale', None)
    if header_lcl in app.config['LANGUAGES']:
        return header_lcl

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    checks user's time zone or defaults to the config
    BABEL_DEFAULT_TIMEZONE.
    """
    timezn = request.args.get('timezone', '').strip()
    if not timezn and g.user:
        timezn = g.user['timezone']

    try:
        return pytz.timezone(timezn).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


"""
    main point of entry
"""
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
