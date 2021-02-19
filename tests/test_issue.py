import unittest
from tests.base_test import BaseTest
from avista_data.issue import Issue
from avista_data.issue_type import IssueType
from avista_data.device import Device


class IssueTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Issue()
        self.fixture.set_name("Test")
        self.fixture.set_description("Test")
        self.fixture.set_type(IssueType.EQUIP_DAMAGED)
        self.db.add(self.fixture)
        self.db.commit()

    def test_id(self):
        self.assertEqual(1, self.fixture.get_id(), "id's do not match")

    def test_name(self):
        self.db.add(self.fixture)
        self.db.commit()
        self.assertEqual("Test", self.fixture.get_name(), "names do not match")

    def test_null_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name(None)

    def test_empty_name(self):
        with self.assertRaises(Exception):
            self.fixture.set_name("")

    def test_description(self):
        self.fixture.set_name("Test")
        self.assertEqual("Test", self.fixture.get_description(), "descriptions do not match")

    def test_null_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description(None)

    def test_empty_description(self):
        with self.assertRaises(Exception):
            self.fixture.set_description("")

    def test_type(self):
        self.assertEqual(IssueType.EQUIP_DAMAGED, self.fixture.get_type(), "descriptions do not match")

    def test_null_type(self):
        with self.assertRaises(Exception):
            self.fixture.set_type(None)

    def test_device(self):
        dev = Device(name="Test Device", description="Description")
        self.db.add(dev)
        dev.add_issue(self.fixture)
        self.assertIn(self.fixture, dev.issues, "issue not added")
        self.assertEqual(dev.get_id(), self.fixture.device_id, "id mismatch")

    def test_to_dict(self):
        exp = {
            "id": 1,
            "name": "Test",
            "description": "Test",
            "type": str(IssueType.EQUIP_DAMAGED)
        }
        self.assertDictEqual(exp, self.fixture.to_dict(), "dicts not the same")

    def test_update(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "Test2",
            "type": str(IssueType.MAINT_REQD)
        }
        self.fixture.update(exp)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not same")
        self.assertEqual(exp['type'], str(self.fixture.get_type()), "type not same")

    def test_create_from_json(self):
        exp = {
            "id": 1,
            "name": "Test2",
            "description": "Test2",
            "type": str(IssueType.MAINT_REQD)
        }
        self.fixture = Issue(exp)
        self.assertEqual(exp['name'], self.fixture.get_name(), "name not same")
        self.assertEqual(exp['description'], self.fixture.get_description(), "desc not same")
        self.assertEqual(exp['type'], str(self.fixture.get_type()), "type not same")

    def test_repr(self):
        self.assertEqual("Issue: Test", self.fixture.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Issue: Test", str(self.fixture), "string representation not same")


if __name__ == '__main__':
    unittest.main()
