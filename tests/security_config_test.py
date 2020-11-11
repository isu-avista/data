import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.security_config import SecurityConfig
from avista_data.device import Device
from avista_data.config_item import ConfigItem
from avista_data.user import User
from avista_data.role import Role


class SecurityConfigTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = SecurityConfig()
        self.fixture.set_name("Test")

    def test_id(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_name(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_name(), "Test", "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_device(self):
        dev = Device(name="Test Device", description="Description")
        db.session.add(dev)
        dev.set_sec_conf(self.fixture)
        self.assertEqual(self.fixture, dev.get_sec_conf(), "security conf not set")

    def test_items(self):
        iss1 = ConfigItem(name="Issue 01", description="Desc 01", value="Value 1")
        iss2 = ConfigItem(name="Issue 02", description="Desc 02", value="Value 2")
        db.session.add(iss1)
        db.session.add(iss2)
        self.fixture.add_item(iss1)
        self.fixture.add_item(iss2)
        self.assertIn(iss1, self.fixture.items)
        self.assertIn(iss2, self.fixture.items)

    def test_users(self):
        u1 = User(first_name="John", last_name="Smith", email="js@example.com", role=Role.USER)
        u1.set_password("test")
        u2 = User(first_name="Jane", last_name="Smith", email="janes@example.com", role=Role.USER)
        u2.set_password("test")
        db.session.add(u1)
        db.session.add(u2)
        self.fixture.add_user(u1)
        self.fixture.add_user(u2)
        self.assertIn(u1, self.fixture.users)
        self.assertIn(u2, self.fixture.users)


if __name__ == '__main__':
    unittest.main()
