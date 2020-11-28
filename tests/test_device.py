import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.device import Device
from avista_data.security_config import SecurityConfig
from avista_data.server_config import ServerConfig
from avista_data.issue import Issue
from avista_data.issue_type import IssueType
from avista_data.sensor import Sensor
from avista_data.unit import Unit
from flask import jsonify


class DeviceTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Device()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_location("Test")
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

    def test_location(self):
        self.assertEqual(self.fixture.get_location(), "Test", "values do not match")

    def test_null_location(self):
        with self.assertRaises(Exception):
            self.fixture.set_location(None)

    def test_empty_location(self):
        with self.assertRaises(Exception):
            self.fixture.set_location("")

    def test_sec_conf(self):
        sc = SecurityConfig(name="SC_Test")
        db.session.add(sc)
        self.fixture.set_sec_conf(sc)
        self.assertEqual(sc, self.fixture.get_sec_conf(), "sec_conf mismatch")

    def test_null_sec_conf(self):
        sc = None
        self.fixture.set_sec_conf(sc)
        self.assertTrue(self.fixture.sec_conf is None, "sec_conf mismatch")

    def test_serv_conf(self):
        sc = ServerConfig(name="SC_Test")
        db.session.add(sc)
        self.fixture.set_serv_conf(sc)
        self.assertEqual(sc, self.fixture.get_serv_conf(), "serv_conf mismatch")

    def test_null_serv_conf(self):
        sc = None
        self.fixture.set_serv_conf(sc)
        self.assertTrue(self.fixture.serv_conf is None, "serv_conf mismatch")

    def test_issues(self):
        iss1 = Issue(name="Issue 01", description="Desc 01", type=IssueType.EQUIP_DAMAGED)
        iss2 = Issue(name="Issue 02", description="Desc 02", type=IssueType.EQUIP_DAMAGED)
        db.session.add(iss1)
        db.session.add(iss2)
        self.fixture.add_issue(iss1)
        self.fixture.add_issue(iss2)
        self.assertIn(iss1, self.fixture.issues)
        self.assertIn(iss2, self.fixture.issues)

    def test_null_issue(self):
        iss = None
        self.fixture.add_issue(iss)
        self.assertEqual(0, self.fixture.issues.count(), "count mismatch")

    def test_sensors(self):
        sens1 = Sensor(name="Sensor 01", quantity="Quantity 01", cls="class1", unit=Unit.C)
        sens2 = Sensor(name="Sensor 02", quantity="Quantity 02", cls="class2", unit=Unit.kWh)
        db.session.add(sens1)
        db.session.add(sens2)
        self.fixture.add_sensor(sens1)
        self.fixture.add_sensor(sens2)
        self.assertIn(sens1, self.fixture.sensors)
        self.assertIn(sens2, self.fixture.sensors)

    def test_null_sensor(self):
        sensor = None
        self.fixture.add_sensor(sensor)
        self.assertEqual(0, self.fixture.sensors.count(), "count mismatch")

    def test_to_dict(self):
        exp = {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "location": "Test"
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "description",
            "location": "location"
        }
        json = jsonify(exp).get_json()
        self.fixture.update(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not the same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not the same")
        self.assertEqual(exp['location'], self.fixture.get_location(), "loc not the same")

    def test_creat_from_json(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "description",
            "location": "location"
        }
        json = jsonify(exp).get_json()
        self.fixture = Device(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not the same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not the same")
        self.assertEqual(exp['location'], self.fixture.get_location(), "loc not the same")

    def test_repr(self):
        self.assertEqual("Device: Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Device: Test", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
