from flask import current_app
from flask import g
from avista_data import db
from avista_data import migrate
import avista_data


def get_db():
    """Gets the current database object, also adds this object to the flask app's global context

    Returns:
        Database object
    """
    if "db" not in g:
        g.db = db
        avista_data.db = g.db
    if "migrate" not in g:
        g.migrate = migrate

    return g.db


def init():
    """Initializes the database and migrate components to use the current flask app"""
    db = get_db()
    db.init_app(current_app)
    g.migrate.init_app(current_app, db=db, render_as_batch=True)

