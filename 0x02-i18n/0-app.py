#!/usr/bin/env python3
"""
Below initializes the flask app
setup a basic Flask app in 0-apppy below
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Create a single / route
    outputs
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
