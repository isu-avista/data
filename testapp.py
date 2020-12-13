from flask import Flask

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask("tests")
app.app_context().push() # don't forget to push the app context
app.config.from_object(Config)

import avista_data
from avista_data import data_manager

data_manager.init()


@app.shell_context_processor
def make_shell_context():
    return {'db': data_manager.get_db()}
