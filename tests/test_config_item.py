import unittest
from avista_data import db
from tests.base_test import BaseTest
from avista_data.config_item import ConfigItem
from avista_data.security_config import SecurityConfig
from avista_data.server_config import ServerConfig
from flask import jsonify


class ConfigItemTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = ConfigItem()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_value("Test")
        db.session.add(self.fixture)
        db.session.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_name(self):
        self.assertEqual(self.fixture.get_name(), "Test", "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_empty_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name("")

    def test_description(self):
        self.fixture.set_name("Test")
        self.assertEqual(self.fixture.get_name(), "Test", "descriptions do not match")

    def test_null_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_empty_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description("")

    def test_value(self):
        self.assertEqual(self.fixture.get_value(), "Test", "values do not match")

    def test_empty_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_parent_security_config(self):
        sc = SecurityConfig(name="SC_Test")
        db.session.add(sc)
        sc.add_item(self.fixture)
        self.assertIn(self.fixture, sc.items, "not contained")
        self.assertEqual(sc.get_id(), self.fixture.sec_conf_id, "id mismatch")

    def test_parent_server_config(self):
        sc = ServerConfig(name="SC_Test")
        db.session.add(sc)
        sc.add_item(self.fixture)
        self.assertIn(self.fixture, sc.items, "not contained")
        self.assertEqual(sc.get_id(), self.fixture.serv_conf_id, "id mismatch")

    def test_to_dict(self):
        exp = {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "value": "Test"
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "Test2",
            "value": "Test2"
        }
        json = jsonify(exp).get_json()
        self.fixture.update(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not same")
        self.assertEqual(exp['value'], self.fixture.get_value(), "value not same")

    def test_create_from_json(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "Test2",
            "value": "Test2"
        }
        json = jsonify(exp).get_json()
        self.fixture = ConfigItem(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not same")
        self.assertEqual(exp['value'], self.fixture.get_value(), "value not same")

    def test_repr(self):
        self.assertEqual("Config Item: Test=Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Config Item: Test=Test", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
