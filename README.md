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
    




