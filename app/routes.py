from flask import render_template

from app import app


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
