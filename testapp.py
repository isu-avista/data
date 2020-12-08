from avista_data.role import Role

from flask import Flask

from avista_data import db
import avista_data
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask("tests")
app.config.from_object(Config)
avista_data.init(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db}
