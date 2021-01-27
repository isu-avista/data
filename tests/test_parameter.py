import unittest
from flask import jsonify
from avista_data import db
from avista_data.parameter import Parameter
from tests.base_test import BaseTest


class ParameterTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Parameter()
        self.fixture.set_key("TestKey")
        self.fixture.set_value("TestValue")
        db.session.add(self.fixture)
        db.session.commit()

    def test_id(self):
        self.assertEqual(self.fixture.get_id(), 1, "ids do not match")

    def test_key(self):
        self.assertEqual(self.fixture.get_key(), "TestKey", "keys do not match")

    def test_null_key(self):
        with self.assertRaises(Exception):
            self.fixture.set_key(None)

    def test_empty_key(self):
        with self.assertRaises(Exception):
            self.fixture.set_key("")

    def test_value(self):
        self.assertEqual(self.fixture.get_value(), "TestValue", "values do not match")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(None)

    def test_empty_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("")

    def test_to_dict(self):
        expected = {
            "id": 1,
            "key": "TestKey",
            "value": "TestValue",
        }
        self.assertDictEqual(expected, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        expected = {
            "id": 1,
            "key": "TestKey2",
            "value": "TestValue2",
        }
        json = jsonify(expected).get_json()
        self.fixture.update(json)
        self.assertEqual(expected['key'], self.fixture.get_key(), "key not the same")
        self.assertEqual(expected['value'], self.fixture.get_value(), "value not the same")

    def test_create_from_json(self):
        expected = {
            "id": 1,
            "key": "TestKey",
            "value": "TestValue",
        }
        json = jsonify(expected).get_json()
        self.fixture = Parameter(json)
        self.assertEqual(expected['key'], self.fixture.get_key(), "key not the same")
        self.assertEqual(expected['value'], self.fixture.get_value(), "value not the same")
