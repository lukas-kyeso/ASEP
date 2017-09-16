from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/our_campaign')
def our_campaign():
    return render_template("our_campaign.html",
                           title='Our Campaign')

@app.route('/who_we_are')
def who_we_are():
    return render_template("who_we_are.html",
                           title='Who We Are')

@app.route('/take_action')
def take_action():
    return render_template("take_action.html",
                           title='Take Action')

@app.route('/news')
def news():
    return render_template("news.html",
                           title='News')

@app.route('/available_support')
def available_support():
    return render_template("available_support.html",
                           title='Available Support')