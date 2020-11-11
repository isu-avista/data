import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.data_point import DataPoint


class DataPointTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = DataPoint()
        self.fixture.set_value(0.0)

    def test_id(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.id, 1, "id's do not match")

    def test_value(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertAlmostEqual(self.fixture.get_value(), 0, 3, "values do not match")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value(None)

    def test_nonfloat_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("Test")

    # def test_parent_security_config(self):

if __name__ == '__main__':
    unittest.main()
