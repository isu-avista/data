import unittest
from tests.base_test import BaseTest
from avista_data.api_key import ApiKey
from avista_data.user import User
from avista_data.role import Role
from avista_data.server import Server
from flask import jsonify


class ApiKeyTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = ApiKey()
        self.fixture.set_key("testkey")
        self.fixture.set_description("Test Key")
        self.db.session.add(self.fixture)
        self.db.session.commit()

    def test_id(self):
        self.assertEqual(1, self.fixture.get_id(), "id's do not match")

    def test_description(self):
        self.assertEqual("Test Key", self.fixture.get_description(), "names do not match")

    def test_null_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_empty_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description("")

    def test_key_hashing(self):
        self.fixture.set_key('cat')
        self.assertFalse(self.fixture.check_key('dog'))
        self.assertTrue(self.fixture.check_key('cat'))

    def test_parent_user(self):
        user = User()
        user.set_first_name("First")
        user.set_last_name("Last")
        user.set_email("email")
        user.set_password("password")
        user.set_role(Role.USER)
        self.db.session.add(user)
        self.db.session.commit()
        user.add_api_key(self.fixture)
        self.assertEqual(user, self.fixture.user, "users are not the same")

    def test_parent_server(self):
        server = Server()
        server.set_name("Test")
        server.set_ip_address("127.0.0.1")
        server.set_port(5000)
        server.set_periodicity(5000)
        self.db.session.add(server)
        self.db.session.commit()
        server.add_api_key(self.fixture)
        self.assertEqual(server, self.fixture.server, "servers are not the same")

    def test_to_dict(self):
        expected = {
            "id": 1,
            "description": "Test Key"
        }
        result = self.fixture.to_dict()
        self.assertDictEqual(expected, result, "dicts not the same")

    def test_update(self):
        expected = {
            "id": 1,
            "description": "Test Key2",
            "key": "New Key"
        }
        json = jsonify(expected).get_json()
        self.fixture.update(json)
        self.assertEqual(expected["description"], self.fixture.get_description())
        self.assertTrue(self.fixture.check_key(expected['key']))

    def test_create_from_json(self):
        expected = {
            "id": 1,
            "description": "Test Key2",
            "key": "New Key"
        }
        json = jsonify(expected).get_json()
        self.fixture = ApiKey(json)
        self.assertEqual(expected["description"], self.fixture.get_description())
        self.assertTrue(self.fixture.check_key(expected['key']))

    def test_repr(self):
        self.assertEqual("API Key: Test Key", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("API Key: Test Key", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
