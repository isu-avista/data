import unittest
from tests.base_test import BaseTest
from avista_data.server_config import ServerConfig
from avista_data.device import Device
from avista_data.config_item import ConfigItem


class ServerConfigTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = ServerConfig()
        self.fixture.set_name("Test")
        self.db.add(self.fixture)
        self.db.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_name(self):
        self.assertEqual(self.fixture.get_name(), "Test", "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_device(self):
        dev = Device(name="Test Device", description="Description")
        self.db.add(dev)
        dev.set_serv_conf(self.fixture)
        self.assertEqual(self.fixture, dev.get_serv_conf(), "server conf not set")

    def test_items(self):
        iss1 = ConfigItem(name="Issue 01", description="Desc 01", value="Value 1")
        iss2 = ConfigItem(name="Issue 02", description="Desc 02", value="Value 2")
        self.db.add(iss1)
        self.db.add(iss2)
        self.fixture.add_item(iss1)
        self.fixture.add_item(iss2)
        self.db.commit()
        self.assertIn(iss1, self.fixture.items)
        self.assertIn(iss2, self.fixture.items)

    def test_null_item(self):
        iss1 = None
        self.fixture.add_item(iss1)
        self.assertEqual(0, self.fixture.items.count(), "counts not same")

    def test_existing_item(self):
        iss1 = ConfigItem(name="Issue 01", description="Desc 01", value="Value 1")
        self.db.add(iss1)
        self.fixture.add_item(iss1)
        count = self.fixture.items.count()
        self.fixture.add_item(iss1)
        self.assertEqual(count, self.fixture.items.count(), "counts not same")

    def test_to_dict(self):
        exp = {
            "id": 1,
            "name": "Test",
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "name": "Test2",
        }
        self.fixture.update(exp)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")

    def test_create_from_json(self):
        exp = {
            "id": 1,
            "name": "Test2",
        }
        self.fixture = ServerConfig(exp)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")

    def test_repr(self):
        self.assertEqual("Server Config: Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Server Config: Test", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
