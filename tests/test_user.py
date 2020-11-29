import unittest
from flask import jsonify
from avista_data.device import Device
from tests.base_test import BaseTest
from avista_data import db
from avista_data.user import User
from avista_data.role import Role
from avista_data.api_key import ApiKey


class UserTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = User()
        self.fixture.set_first_name("First")
        self.fixture.set_last_name("Last")
        self.fixture.set_email("email")
        self.fixture.set_password("password")
        self.fixture.set_role(Role.USER)
        db.session.add(self.fixture)
        db.session.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_first_name(self):
        self.assertEqual(self.fixture.get_first_name(), "First", "names do not match")

    def test_null_first_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_first_name(None)

    def test_empty_first_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_first_name("")

    def test_last_name(self):
        self.assertEqual(self.fixture.get_last_name(), "Last", "names do not match")

    def test_null_last_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_last_name(None)

    def test_empty_last_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_last_name("")

    def test_email(self):
        self.assertEqual(self.fixture.get_email(), "email", "names do not match")

    def test_null_email(self):
        with self.assertRaises(Exception):
            self.fixture.set_email(None)

    def test_empty_email(self):
        with self.assertRaises(Exception):
            self.fixture.set_email("")

    def test_role(self):
        self.assertEqual(self.fixture.get_role(), Role.USER, "roles do not match")

    def test_null_role(self):
        with self.assertRaises(Exception):
            self.fixture.set_role(None)

    def test_password_hashing(self):
        self.fixture.set_password('cat')
        self.assertFalse(self.fixture.check_password('dog'))
        self.assertTrue(self.fixture.check_password('cat'))

    def test_api_key(self):
        key = ApiKey()
        key.set_key("testkey")
        key.set_description("Test Key")
        db.session.add(key)
        self.fixture.add_api_key(key)
        self.assertEqual(1, self.fixture.api_keys.count(), "counts are same")
        self.assertIn(key, self.fixture.api_keys, "key not found")

    def test_null_api_key(self):
        self.fixture.add_api_key(None)
        self.assertEqual(0, self.fixture.api_keys.count(), "counts are same")

    def test_existing_api_key(self):
        key = ApiKey()
        key.set_key("testkey")
        key.set_description("Test Key")
        db.session.add(key)
        self.fixture.add_api_key(key)
        self.fixture.add_api_key(key)
        self.assertEqual(1, self.fixture.api_keys.count(), "counts are same")

    def test_device(self):
        sc = Device(name="SC_Test")
        db.session.add(sc)
        sc.add_user(self.fixture)
        db.session.commit()
        self.assertIn(self.fixture, sc.users, "user not added")
        self.assertEqual(self.fixture.device_id, sc.get_id(), "id mismatch")

    def test_to_dict(self):
        expected = {
            "id": 1,
            "first_name": "First",
            "last_name": "Last",
            "email": "email",
            "role": str(Role.USER)
        }
        result = self.fixture.to_dict()
        self.assertDictEqual(expected, result, "dicts not the same")

    def test_update(self):
        expected = {
            "first_name": "First2",
            "last_name": "Last2",
            "email": "email2",
            "password": "password2",
            "role": str(Role.ADMIN)
        }
        json = jsonify(expected).get_json()
        self.fixture.update(json)
        self.assertEqual(expected["first_name"], self.fixture.get_first_name())
        self.assertEqual(expected["last_name"], self.fixture.get_last_name())
        self.assertEqual(expected["email"], self.fixture.get_email())
        self.assertEqual(Role.from_str(expected["role"]), self.fixture.get_role())
        self.assertTrue(self.fixture.check_password(expected['password']))


    def test_create_from_json(self):
        expected = {
            "id": 2,
            "first_name": "First",
            "last_name": "Last",
            "email": "email",
            "password": "password",
            "role": str(Role.USER)
        }
        json = jsonify(expected).get_json()
        self.fixture = User(json)
        self.assertEqual(expected["first_name"], self.fixture.get_first_name())
        self.assertEqual(expected["last_name"], self.fixture.get_last_name())
        self.assertEqual(expected["email"], self.fixture.get_email())
        self.assertEqual(Role.from_str(expected["role"]), self.fixture.get_role())
        self.assertTrue(self.fixture.check_password(expected['password']))

    def test_repr(self):
        self.assertEqual("User: email", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("User: email", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
