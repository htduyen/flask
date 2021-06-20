# flask
Learn basic flask

# Chapter 4:
When some thing wrong and no solution we can remove folders ``migrations`` and ``db file`` in config.py
    Since I have updates to the application models, a new database migration needs to be generated:
    
    >>> flask db migrate -m "posts table"
Migrate can be fail if we change other model without ``migrate`` and ``upgrade``

And the migration needs to be applied to the database:
    
    >>> flask db upgrade

Play Time: We should use terminal

    (venv)>>>python    

    >>> from app import db
    >>> from app.models import User, Post

    >>> u = User(username='htduyen', email='htduyen@example.com')
    >>> db.session.add(u)
    >>> db.session.commit()

If at any time while working on a session there is an error, a call to ``db.session.rollback()`` will abort the session and remove any changes stored in it. 
And ``db.session.commit()`` is called.

A query returns all the users:

    >>> users = User.query.all()
    >>> users
    >>> for u in users:
    ...     print(u.id, u.username)


#Chapter 5: Login-page
5.1: Password Hashing:   Werkzeug package

Example: 

    >>> from werkzeug.security import generate_password_hash
    >>> hash = generate_password_hash('foobar')

    >>> from werkzeug.security import check_password_hash
    >>> check_password_hash(hash, 'foobar')

5.2: Flask-Login

* Manages the user logged-in state.
* Provides the "remember me" functionality.
* Allows users to remain logged in even after closing the browser window.


    pip install flask-login

* UserMixin: Implementations is_authenticated, is_active, is_anonymous properties and get_id() method 


* @login.user_loader: registered with Flask-Login

* In login page If the username and password are both correct, then I call the ``login_user()`` function, which comes from Flask-Login. This function will register the user as logged in, so that means that any future pages the user navigates to will have the ``current_user`` variable set to that user.

* @login_required: against anonymous users is with a decorator

# Chapter 6: Profile Page and Avatars

# Chapter 7: Error Handling

Using dedug mode:

    export FLASK_DEBUG=1
    set FLASK_DEBUG=1 (Window)
    flask run

Off debug mode:

    set FLASK_DEBUG=0

Sending Errors by Email:

    Less secure app access: On (Setting on your gmail)

Logs file

# Chapter 8: Followers

    Cross-site request forgery: CSRF is also used as an abbreviation in defences against CSRF attacks, 
    such as techniques that use header data, form data, or cookies, to test for and prevent such attacks.

 It would be easier to implement these routes as GET requests, 
 but then they could be exploited in CSRF attacks. 
 Because GET requests are harder to protect against CSRF, 
 they should only be used on actions that do not introduce state changes.

# Chapter 9: Pagination
    
    https://en.wikipedia.org/wiki/Post/Redirect/Get

# Chapter 10: Email Support
    
    DOC: https://pythonhosted.org/Flask-Mail/

    As far as the actual sending of emails, Flask has a popular extension called Flask-Mail that can make the task very easy. As always, this extension is installed with pip:
        
        pip install flask-mail
    
    The password reset links will have a secure token in them.
    I'm going to use JSON Web Tokens, which also have a popular Python package:
            
        pip install pyjwt

We can start in a second terminal with the following command:
    
    python -m smtpd -n -c DebuggingServer localhost:8025

The Flask-Mail extension is configured from the app.config object.
To configure for this server you will need to set two environment variables:
        
    export MAIL_SERVER=localhost
    export MAIL_PORT=8025

If you prefer to have emails sent for real, you need to use a real email server. If you have one, then you just need to set the MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME and MAIL_PASSWORD environment variables for it
    
    (venv) $ export MAIL_SERVER=smtp.googlemail.com
    (venv) $ export MAIL_PORT=587
    (venv) $ export MAIL_USE_TLS=1
    (venv) $ export MAIL_USERNAME=<your-gmail-username>
    (venv) $ export MAIL_PASSWORD=<your-gmail-password>


..Note: allow "less secure apps" access to your Gmail account. 
    
    https://support.google.com/accounts/answer/6010255?hl=en
    
Flask-Mail Usage with ``flask shell``
    
    >>> from flask_mail import Message
    >>> from app import mail
    >>> msg = Message('test subject', sender=app.config['ADMINS'][0],
    ... recipients=['your-email@example.com'])
    >>> msg.body = 'text body'
    >>> msg.html = '<h1>HTML body</h1>'
    >>> mail.send(msg)

Requesting a Password Reset: A very popular token standard for this type of process is the JSON Web Token, or JWT.
    
    >>> import jwt
    >>> token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
    >>> token
    'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
    >>> jwt.decode(token, 'my-secret', algorithms=['HS256'])
    {'a': 'b'}

# Chapter 11: Facelift - Bootstrap


# Chapter 12: Datetime

Moment.js is a small open-source JavaScript library that takes date and time rendering to another level
The moment object provides several methods for different rendering options. Below are some of the most common options:
    
    moment('2017-09-28T21:45:23Z').format('L')
    "09/28/2017"
    moment('2017-09-28T21:45:23Z').format('LL')
    "September 28, 2017"
    moment('2017-09-28T21:45:23Z').format('LLL')
    "September 28, 2017 2:45 PM"
    moment('2017-09-28T21:45:23Z').format('LLLL')
    "Thursday, September 28, 2017 2:45 PM"
    moment('2017-09-28T21:45:23Z').format('dddd')
    "Thursday"
    moment('2017-09-28T21:45:23Z').fromNow()
    "7 hours ago"
    moment('2017-09-28T21:45:23Z').calendar()
    "Today at 2:45 PM"

