import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.security_config import SecurityConfig


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

    # def test_device(self):

    # def test_items(self):

    # def test_users(self):


if __name__ == '__main__':
    unittest.main()
