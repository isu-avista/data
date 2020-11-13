import unittest

from avista_data.security_config import SecurityConfig
from tests.base_test import BaseTest
from avista_data import db
from avista_data.user import User
from avista_data.role import Role


class MyTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = User()
        self.fixture.set_first_name("First")
        self.fixture.set_last_name("Last")
        self.fixture.set_email("email")
        self.fixture.set_password("password")
        self.fixture.set_role(Role.USER)

    def test_id(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_first_name(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_first_name(), "First", "names do not match")

    def test_null_first_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_first_name(None)

    def test_empty_first_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_first_name("")

    def test_last_name(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_last_name(), "Last", "names do not match")

    def test_null_last_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_last_name(None)

    def test_empty_last_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_last_name("")

    def test_email(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_email(), "email", "names do not match")

    def test_null_email(self):
        with self.assertRaises(Exception):
            self.fixture.set_email(None)

    def test_empty_email(self):
        with self.assertRaises(Exception):
            self.fixture.set_email("")

    def test_role(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_role(), Role.USER, "roles do not match")

    def test_null_role(self):
        with self.assertRaises(Exception):
            self.fixture.set_role(None)

    def test_password_hashing(self):
        self.fixture.set_password('cat')
        self.assertFalse(self.fixture.check_password('dog'))
        self.assertTrue(self.fixture.check_password('cat'))

    # def test_token(self):

    def test_security_config(self):
        sc = SecurityConfig(name="SC_Test")
        db.session.add(sc)
        sc.add_user(self.fixture)
        db.session.commit()
        self.assertIn(self.fixture, sc.users, "user not added")
        self.assertEqual(self.fixture.sec_conf_id, sc.get_id(), "id mismatch")

if __name__ == '__main__':
    unittest.main()
