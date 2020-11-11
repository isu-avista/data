import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.device import Device

class DeviceTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Device()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_location("Test")

    def test_id(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.id, 1, "id's do not match")

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

    def test_location(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_location(), "Test", "values do not match")

    def test_empty_location(self):
        with self.assertRaises(Exception):
            self.fixture.set_value("")

    def test_null_value(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    # def test_sec_conf(self):

    # def test_serv_conf(self):

    # def test_issues(self):

if __name__ == '__main__':
    unittest.main()
