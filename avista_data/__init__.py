"""The ISU Avista Data Module which contains the basic classes used to interface between the system and the database.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from avista_data import config_item
from avista_data import data_point
from avista_data import device
from avista_data import issue
from avista_data import security_config
from avista_data import server_config
from avista_data import sensor
from avista_data import user
from avista_data import pin_out
from avista_data import server
from avista_data import status
from avista_data import api_key
from avista_data import role_too_low_error


def init(app):
    """Initializes the module with the provided Flask App

    Args:
        app (:obj: `Flask`): The Flask app which uses this module
    """
    db.init_app(app)
    migrate.init_app(app, db=db, render_as_batch=True)
