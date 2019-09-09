from random import choice, sample
from flask import flask
from flask import render_template

app = flask(__name__)

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    section = 'BEW 1.1'
    greeting = 'Good morning'
    return render_template('gif-search.html'
    section=section, greeting=greeting)

@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliment = choice(compliments)
    compliments_to_show = sample(compliments, 3)

    return render_template(
        'gif-search.html',
        name=name,
        show_compliments=show_compliments,
        compliment=compliment,
        compliment=compliments_to_show)
