import unittest

from avista_data.unit import Unit
from tests.base_test import BaseTest
from avista_data.sensor import Sensor
from avista_data import db
from avista_data.device import Device
from avista_data.data_point import DataPoint
from avista_data.pin_out import PinOut
from datetime import datetime
from flask import jsonify


class SensorTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Sensor()
        self.fixture.set_name("Test")
        self.fixture.set_quantity("Test")
        self.fixture.set_class("Test")
        self.fixture.set_module('test.test')
        self.fixture.set_unit(Unit.kWh)

        self.fixture.add_pin_out(PinOut(var="t", pin=1))
        db.session.add(self.fixture)
        db.session.commit()

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

    def test_cls(self):
        self.assertEqual("Test", self.fixture.get_class(), "classes do not match")

    def test_null_cls(self):
        with self.assertRaises(Exception):
            self.fixture.set_class(None)

    def test_empty_cls(self):
        with self.assertRaises(Exception):
            self.fixture.set_class("")

    def test_module(self):
        self.assertEqual("test.test", self.fixture.get_module(), "modules do not match")

    def test_null_module(self):
        with self.assertRaises(Exception):
            self.fixture.set_module(None)

    def test_empty_module(self):
        with self.assertRaises(Exception):
            self.fixture.set_module("")

    def test_unit(self):
        self.assertEqual(Unit.kWh, self.fixture.get_unit(), "names do not match")

    def test_null_unit(self):
        with self.assertRaises(Exception):
            self.fixture.set_unit(None)

    def test_quantity(self):
        self.fixture.set_quantity("Test2")
        self.assertEqual("Test2", self.fixture.get_quantity(), "quantities do not match")

    def test_null_quantity(self):
        with self.assertRaises(Exception):
            self.fixture.set_quantity(None)

    def test_empty_quantity(self):
        with self.assertRaises(Exception):
            self.fixture.set_quantity("")

    def test_device(self):
        dev = Device(name="Test Device", description="Description")
        db.session.add(dev)
        db.session.commit()
        dev.add_sensor(self.fixture)
        self.assertIn(self.fixture, dev.sensors, "sensor not added")
        self.assertEqual(dev.get_id(), self.fixture.device_id, "id mismatch")

    def test_update(self):
        d = self.fixture.to_dict()
        d['name'] = "Test2"
        d['quantity'] = "Vibration"
        self.fixture.update(jsonify(d).get_json())
        self.assertEqual("Test2", self.fixture.get_name(), "new names are not same")
        self.assertEqual("Vibration", self.fixture.get_quantity(), "new quantity not the same")

    def test_data(self):
        dp = DataPoint(value=1.0, timestamp=int(datetime.timestamp(datetime.now())))
        db.session.add(dp)
        self.fixture.add_data_point(dp)
        self.assertIn(dp, self.fixture.data, "point not contained")

    def test_null_data(self):
        count = self.fixture.data.count()
        self.fixture.add_data_point(None)
        self.assertEqual(count, self.fixture.data.count(), "counts are not the same")

    def test_know_data_point(self):
        dp = DataPoint(value=1.0, timestamp=int(datetime.timestamp(datetime.now())))
        db.session.add(dp)
        self.fixture.add_data_point(dp)
        count = self.fixture.data.count()
        self.fixture.add_data_point(dp)
        self.assertEqual(count, self.fixture.data.count(), "counts are not the same")

    def test_pin_out(self):
        po = PinOut(var="test", pin=2)
        db.session.add(po)
        self.fixture.add_pin_out(po)
        self.assertEqual(2, self.fixture.pinout.count(), "size changed")

    def test_null_pin_out(self):
        po = None
        self.fixture.add_pin_out(po)
        self.assertEqual(1, self.fixture.pinout.count(), "size changed")

    def test_existing_pin_out(self):
        po = self.fixture.pinout[0]
        self.fixture.add_pin_out(po)
        self.assertEqual(1, self.fixture.pinout.count(), "size changed")

    def test_to_dict(self):
        exp = {
            'id': 1,
            'name': 'Test',
            'quantity': 'Test',
            'module': 'test.test',
            'cls': 'Test',
            'unit': 'kWh',
            'pinout': [
                {
                    'id': 1,
                    'var': 't',
                    'pin': 1
                }
            ]
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts are not equal")

    def test_repr(self):
        self.assertEqual("Sensor: Test = Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Sensor: Test = Test", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
