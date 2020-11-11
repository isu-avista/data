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


def init(app):
    db.init_app(app)
    migrate.init_app(app, db=db, render_as_batch=True)
