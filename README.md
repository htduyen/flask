# flask
Learn basic flask

Chapter 4: When some thing wrong and no solution we can remove folders ``migrations`` and ``db file`` in config.py
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



