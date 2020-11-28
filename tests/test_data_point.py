import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.data_point import DataPoint
from avista_data.sensor import Sensor
from datetime import datetime
from avista_data.unit import Unit
from flask import jsonify


class DataPointTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = DataPoint()
        self.fixture.set_value(0.0)
        self.fixture.set_timestamp(int(datetime.timestamp(datetime.now())))
        db.session.add(self.fixture)
        db.session.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_value(self):
        self.assertAlmostEqual(self.fixture.get_value(), 0, 3, "values do not match")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(None)

    def test_nonfloat_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("Test")

    def test_parent_sensor(self):
        sens = Sensor(name="TestSensor", quantity="Power", unit=Unit.kWh)
        db.session.add(sens)
        sens.add_data_point(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.sensor_id, sens.get_id(), "id mismatch")

    def test_timestamp(self):
        self.assertEqual(int(datetime.timestamp(datetime.now())), self.fixture.get_timestamp(), "timestamps do not match")

    def test_non_int_timestamp(self):
        with self.assertRaises(Exception):
            self.fixture.set_timestamp("001")

    def test_null_timestamp(self):
        with self.assertRaises(Exception):
            self.fixture.set_timestamp(None)

    def test_repr(self):
        self.assertEqual("Data Point: 0.0", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Data Point: 0.0", str(self.fixture), "string representation not same")

    def test_to_dict(self):
        exp = {
            "id": 1,
            "value": 0.0,
            "timestamp": int(datetime.timestamp(datetime.now()))
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "value": 2.0,
            "timestamp": 10
        }
        json = jsonify(exp).get_json()
        self.fixture.update(json)
        self.assertEqual(exp['id'], self.fixture.get_id())
        self.assertAlmostEqual(exp['value'], self.fixture.get_value(), 3)
        self.assertEqual(exp['timestamp'], self.fixture.get_timestamp())

    def test_create_from_json(self):
        exp = {
            "id": 2,
            "value": 2.0,
            "timestamp": 10
        }
        json = jsonify(exp).get_json()
        self.fixture = DataPoint(json)
        self.assertAlmostEqual(exp['value'], self.fixture.get_value(), 3)
        self.assertEqual(exp['timestamp'], self.fixture.get_timestamp())


if __name__ == '__main__':
    unittest.main()
