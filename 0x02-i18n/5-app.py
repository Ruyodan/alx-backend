#!/usr/bin/env python3
"""Module containing Flask app with Babel integration"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Class that defines Babel instance attributes"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """Function defining route to html template"""

    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Function to determine the best match with our supported languages"""

    lang = request.args.get('locale')
    langs = app.config['LANGUAGES']

    if lang in langs:
        return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Function that retirns user dictionary"""

    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]

    except Exception:
        return None


@app.before_request
def before_request():
    """Function to use before_request decorator to be executed first"""

    g.user = get_user()


if __name__ == "__main__":
    app.run()
