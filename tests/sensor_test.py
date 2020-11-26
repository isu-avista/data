import unittest

from avista_data.unit import Unit
from tests.base_test import BaseTest
from avista_data.sensor import Sensor
from avista_data import db
from avista_data.device import Device
from avista_data.data_point import DataPoint
from datetime import datetime


class SensorTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Sensor()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_identifier("Test")
        self.fixture.set_unit(Unit.KWH)

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

    def test_type(self):
        self.fixture.set_name("Test")
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_name(), "Test", "descriptions do not match")

    def test_null_type(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_device(self):
        dev = Device(name="Test Device", description="Description")
        db.session.add(dev)
        dev.add_sensor(self.fixture)
        self.assertIn(self.fixture, dev.sensors, "sensor not added")
        self.assertEqual(self.fixture.device_id, dev.get_id(), "id mismatch")

    def test_data(self):
        dp = DataPoint(value=1.0, timestamp=int(datetime.timestamp(datetime.now())))
        db.session.add(dp)
        self.fixture.add_data_point(dp)
        db.session.commit()
        self.assertIn(dp, self.fixture.data, "point not contained")


if __name__ == '__main__':
    unittest.main()
