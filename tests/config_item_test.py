import unittest
from avista_data import db
from tests.base_test import BaseTest
from avista_data.config_item import ConfigItem
from avista_data.security_config import SecurityConfig
from avista_data.server_config import ServerConfig


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

    def test_parent_security_config(self):
        sc = SecurityConfig(name="SC_Test")
        db.session.add(sc)
        sc.add_item(self.fixture)
        db.session.commit()
        self.assertIn(self.fixture, sc.items, "not contained")
        self.assertEquals(sc.get_id(), self.fixture.sec_conf_id, "id mismatch")

    def test_parent_server_config(self):
        sc = ServerConfig(name="SC_Test")
        db.session.add(sc)
        sc.add_item(self.fixture)
        db.session.commit()
        self.assertIn(self.fixture, sc.items, "not contained")
        self.assertEquals(sc.get_id(), self.fixture.serv_conf_id, "id mismatch")


if __name__ == '__main__':
    unittest.main()
