#!/usr/bin/env python3
"""
below is a basic Flask app with Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    handles configs for supported languages and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en' # language
    BABEL_DEFAULT_TIMEZONE = 'UTC' # time


# Flask app
app = Flask(__name__)
# configuration
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Returns the language specified in query parameter 'locale' if valid
    best match from accepted languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

"""
main point of entry
"""
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    renders the indexhtml template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
