import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.issue import Issue
from avista_data.issue_type import IssueType


class IssueTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Issue()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_type(IssueType.EQUIP_DAMAGED)

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

    def test_type(self):
        db.session.add(self.fixture)
        db.session.commit()
        self.assertEqual(self.fixture.get_type(), IssueType.EQUIP_DAMAGED, "descriptions do not match")

    def test_null_type(self):
        with self.assertRaises(Exception):
            self.fixture.set_type(None)

    # def test_device(self):

if __name__ == '__main__':
    unittest.main()
