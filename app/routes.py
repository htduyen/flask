from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def index():
    title = 'Chapter2'
    persion = {
        'username': 'Huynh Thanh Duyen',
        'age': 24
    }
    posts = [
        {
           'name': 'Duyen Huynh',
           'content': 'Example 1'
        },
        {
           'name': 'Duyen Huynh 2',
           'content': 'Example 2'
        },
        {
           'name': 'Duyen Huynh 3',
           'content': 'Example 3'
        }
    ]
    return render_template('index.html', username=persion['username'], age=persion['age'], posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
