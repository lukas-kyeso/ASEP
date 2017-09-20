#!flask/bin/python
from flask import Flask
from flask import render_template
application = Flask(__name__)

@application.route('/')
@application.route('/index')
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

@application.route('/our_campaign')
def our_campaign():
    return render_template("our_campaign.html",
                           title='Our Campaign')

@application.route('/who_we_are')
def who_we_are():
    return render_template("who_we_are.html",
                           title='Who We Are')

@application.route('/take_action')
def take_action():
    return render_template("take_action.html",
                           title='Take Action')

@application.route('/news')
def news():
    return render_template("news.html",
                           title='News')

@application.route('/available_support')
def available_support():
    return render_template("available_support.html",
                           title='Available Support')

@application.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    application.run(debug = True)
