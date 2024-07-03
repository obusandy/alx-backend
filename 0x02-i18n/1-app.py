#!/usr/bin/env python3
"""
FLASK app
Babel Flask
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    instantiate the Babel object in your app
    create a Config class that has a LANGUAGES
    class attr: equal to ["en", "fr"].
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en' # Use Config to set Babel’s default locale ("en")
    BABEL_DEFAULT_TIMEZONE = 'UTC' # timezone ("UTC").


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config) # instantiate the Babel object in your app

babel = Babel(app)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    route
    """
    return render_template('1-index.html')

"""
main point of entry
"""
if __name__ == '__main__':
    app.run()
