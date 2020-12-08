#!/usr/bin/env python
import unittest
from flask import Flask
import avista_data
import os


def create_app(config):
    app = Flask("Test")
    avista_data.init(app)
    app.config.from_object(config)
    return app


class TestConfig(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRETE_KEY = "TEST_KEY"


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        avista_data.db.create_all()
        avista_data.populate_initial_data(self.app)

    def tearDown(self):
        avista_data.db.session.remove()
        avista_data.db.drop_all()
        self.app_context.pop()
