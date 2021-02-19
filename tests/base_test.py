#!/usr/bin/env python
import unittest
import avista_data.data_manager
import os


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
avista_data.database.init(SQLALCHEMY_DATABASE_URI)

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.db = avista_data.database.db
        print("self.db:", self.db)
        avista_data.database.populate_initial_data()

    def tearDown(self):
        avista_data.database.clear_data()
