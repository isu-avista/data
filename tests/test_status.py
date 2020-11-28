import unittest
from avista_data import db
from avista_data.status import Status
from tests.base_test import BaseTest
from flask import jsonify


class StatusTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Status()
        self.fixture.set_name("Test")
        self.fixture.set_value(1)
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

    def test_value(self):
        self.assertEqual(1, self.fixture.get_value(), "values do not match")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(None)

    def test_below_range_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(-1)

    def test_above_range_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(4)

    def test_to_dict(self):
        exp = {
            'id': 1,
            'name': 'Test',
            'value': 1,
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts are not equal")

    def test_update(self):
        exp = {
            'name': 'Test2',
            'value': 2,
        }
        json = jsonify(exp).get_json()
        self.fixture.update(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "names are not the same")
        self.assertEqual(exp['value'], self.fixture.get_value(), "values are not the same")

    def test_create_from_json(self):
        exp = {
            'name': 'Test2',
            'value': 2,
        }
        json = jsonify(exp).get_json()
        self.fixture = Status(json)
        self.assertEqual(exp['name'], self.fixture.get_name(), "names are not the same")
        self.assertEqual(exp['value'], self.fixture.get_value(), "values are not the same")

    def test_repr(self):
        self.assertEqual("Status: Test = 1", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Status: Test = 1", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
