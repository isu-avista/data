import unittest
from tests.base_test import BaseTest
from avista_data import db
from avista_data.device import Device
from avista_data.security_config import SecurityConfig
from avista_data.server_config import ServerConfig
from avista_data.issue import Issue
from avista_data.issue_type import IssueType

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

    def test_sec_conf(self):
        sc = SecurityConfig(name="SC_Test")
        db.session.add(sc)
        self.fixture.set_sec_conf(sc)
        db.session.commit()
        self.assertEqual(sc, self.fixture.get_sec_conf(), "sec_conf mismatch")

    def test_serv_conf(self):
        sc = ServerConfig(name="SC_Test")
        db.session.add(sc)
        self.fixture.set_serv_conf(sc)
        db.session.commit()
        self.assertEqual(sc, self.fixture.get_serv_conf(), "serv_conf mismatch")

    def test_issues(self):
        iss1 = Issue(name="Issue 01", description="Desc 01", type=IssueType.EQUIP_DAMAGED)
        iss2 = Issue(name="Issue 02", description="Desc 02", type=IssueType.EQUIP_DAMAGED)
        db.session.add(iss1)
        db.session.add(iss2)
        self.fixture.add_issue(iss1)
        self.fixture.add_issue(iss2)
        self.assertIn(iss1, self.fixture.issues)
        self.assertIn(iss2, self.fixture.issues)

if __name__ == '__main__':
    unittest.main()
