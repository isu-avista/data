import unittest
from flask import jsonify
from avista_data import db
from avista_data.pin_out import PinOut
from tests.base_test import BaseTest


class PinOutTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = PinOut()
        self.fixture.set_var("Test")
        self.fixture.set_pin(1)
        db.session.add(self.fixture)
        db.session.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "id's do not match")

    def test_var(self):
        self.assertEqual(self.fixture.get_var(), "Test", "names do not match")

    def test_null_var(self):
        with self.assertRaises(Exception):
            self.fixture.set_var(None)

    def test_empty_var(self):
        with self.assertRaises(Exception):
            self.fixture.set_var("")

    def test_pin(self):
        self.assertEqual(self.fixture.get_pin(), 1, "pins do not match")

    def test_null_pin(self):
        with self.assertRaises(Exception):
            self.fixture.set_pin(None)

    def test_pin_less_than_one(self):
        with self.assertRaises(Exception):
            self.fixture.set_pin(0)

    def test_pin_greater_than_forty(self):
        with self.assertRaises(Exception):
            self.fixture.set_pin(41)

    def test_to_dict(self):
        expected = {
            "id": 1,
            "var": "Test",
            "pin": 1,
        }
        self.assertDictEqual(expected, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "var": "Test2",
            "pin": 2,
        }
        json = jsonify(exp).get_json()
        self.fixture.update(json)
        self.assertEqual(exp['var'], self.fixture.get_var(), "var not the same")
        self.assertEqual(exp['pin'], self.fixture.get_pin(), "pin not the same")

    def test_creat_from_json(self):
        exp = {
            "id": 1,
            "var": "Test2",
            "pin": 2,
        }
        json = jsonify(exp).get_json()
        self.fixture = PinOut(json)
        self.assertEqual(exp['var'], self.fixture.get_var(), "var not the same")
        self.assertEqual(exp['pin'], self.fixture.get_pin(), "pin not the same")

    def test_repr(self):
        self.assertEqual("Pin Out: <Test, 1>", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Pin Out: <Test, 1>", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
