"""The ISU Avista Data Module which contains the basic classes used to interface between the system and the database.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from avista_data import data_manager
from flask import current_app

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
from avista_data.role import Role
from avista_data.user import User


def populate_initial_data():
    with current_app.app_context():
        db = data_manager.get_db()
        data_manager.get_db().create_all()

        if db is not None and User.query.count() == 0:
            admin = User()
            db.session.add(admin)
            User.admin_account_details(admin)
            db.session.commit()
