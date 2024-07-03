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


class Config(object):
    """Config class
    that has a LANGUAGES class attribute
    Holds configurations for languages and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en' # language
    BABEL_DEFAULT_TIMEZONE = 'UTC' # time zone


# flask app
app = Flask(__name__)
app.config.from_object(Config)

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
    """
    users preferred local if it is supported.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Returns the lang specified in query param 'locale' if valid
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

"""
    main point of entry
"""

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run()
