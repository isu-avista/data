import unittest
from avista_data.server import Server
from avista_data.api_key import ApiKey
from tests.base_test import BaseTest


class ServerTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Server()
        self.fixture.set_name("Test")
        self.fixture.set_ip_address("127.0.0.1")
        self.fixture.set_port(5000)
        self.fixture.set_periodicity(5000)
        self.db.add(self.fixture)
        self.db.commit()

    def test_id(self):
        self.assertEqual(1, self.fixture.get_id(), "id's do not match")

    def test_name(self):
        self.assertEqual("Test", self.fixture.get_name(), "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_empty_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name("")

    def test_ip(self):
        self.assertEqual("127.0.0.1", self.fixture.get_ip_address(), "ip addresses are not the same")

    def test_null_ip(self):
        with self.assertRaises(Exception):
            self.fixture.set_ip_address(None)

    def test_empty_ip(self):
        with self.assertRaises(Exception):
            self.fixture.set_ip_address("")

    def test_malformed_ip(self):
        with self.assertRaises(Exception):
            self.fixture.set_ip_address("127.0.1")

    def test_malformed_ip_2(self):
        with self.assertRaises(Exception):
            self.fixture.set_ip_address("test")

    def test_port(self):
        self.assertEqual(5000, self.fixture.get_port(), "ports are not the same")

    def test_null_port(self):
        with self.assertRaises(Exception):
            self.fixture.set_port(None)

    def test_below_range_port(self):
        with self.assertRaises(Exception):
            self.fixture.set_port(0)

    def test_below_range_port_2(self):
        with self.assertRaises(Exception):
            self.fixture.set_port(-1)

    def test_above_range_port(self):
        with self.assertRaises(Exception):
            self.fixture.set_port(65536)

    def test_periodicity(self):
        self.assertEqual(5000, self.fixture.get_periodicity(), "periodicity not the same")

    def test_null_periodicity(self):
        with self.assertRaises(Exception):
            self.fixture.set_periodicity(None)

    def test_below_range_periodicity(self):
        with self.assertRaises(Exception):
            self.fixture.set_periodicity(0)

    def test_below_range_periodicity_2(self):
        with self.assertRaises(Exception):
            self.fixture.set_periodicity(-1)

    def test_api_key(self):
        key = ApiKey()
        key.set_key("testkey")
        key.set_description("Test Key")
        self.db.add(key)
        self.fixture.add_api_key(key)
        self.db.commit()
        self.assertEqual(1, self.fixture.api_keys.count(), "counts are same")
        self.assertIn(key, self.fixture.api_keys, "key not found")

    def test_null_api_key(self):
        self.fixture.add_api_key(None)
        self.assertEqual(0, self.fixture.api_keys.count(), "counts are same")

    def test_existing_api_key(self):
        key = ApiKey()
        key.set_key("testkey")
        key.set_description("Test Key")
        self.db.add(key)
        self.fixture.add_api_key(key)
        self.fixture.add_api_key(key)
        self.db.commit()
        self.assertEqual(1, self.fixture.api_keys.count(), "counts are same")

    def test_to_dict(self):
        exp = {
            'id': 1,
            'name': 'Test',
            'ip_address': '127.0.0.1',
            'port': 5000,
            'periodicity': 5000
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dictionary representation incorrect")

    def test_update(self):
        exp = {
            'name': 'Test2',
            'ip_address': '127.0.1.1',
            'port': 5000,
            'periodicity': 5000
        }
        self.fixture.update(exp)
        self.assertEqual("Test2", self.fixture.get_name(), "names are not the same")
        self.assertEqual("127.0.1.1", self.fixture.get_ip_address(), "ips are not the same")

    def test_create_from_json(self):
        exp = {
            'name': 'Test2',
            'ip_address': '127.0.1.1',
            'port': 5000,
            'periodicity': 5000
        }
        self.fixture = Server(exp)
        self.assertEqual("Test2", self.fixture.get_name(), "names are not the same")
        self.assertEqual("127.0.1.1", self.fixture.get_ip_address(), "ips are not the same")

    def test_repr(self):
        self.assertEqual("Server: Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Server: Test", str(self.fixture), "string representation not same")

if __name__ == '__main__':
    unittest.main()
