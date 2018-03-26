from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Njuguna'}
    posts = [
        {
            'author': {'username': 'James'},
            'body':'This is beautiful'
        },
        {
            'author': {'username': 'Sylvia'},
            'body':'All is well'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)