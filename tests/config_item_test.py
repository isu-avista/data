import unittest
from avista_data import db
from tests.base_test import BaseTest
from avista_data.config_item import ConfigItem


class ConfigItemTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = ConfigItem()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_value("Test")

    def test_id(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.id, 1, "id's do not match")

    def test_name(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_name(), "Test", "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_empty_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name("")

    def test_description(self):
        self.fixture.set_name("Test")
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_name(), "Test", "descriptions do not match")

    def test_null_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_empty_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description("")

    def test_value(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_value(), "Test", "values do not match")

    def test_empty_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    # def test_parent_security_config(self):

    # def test_parent_server_config(self):


if __name__ == '__main__':
    unittest.main()
