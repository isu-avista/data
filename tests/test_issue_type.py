import unittest
from avista_data.issue_type import IssueType


class IssueTypeTest(unittest.TestCase):

    def test_from_str(self):
        oracle = [
            ["MAINT_REQD", IssueType.MAINT_REQD],
            ["maint_reqd", IssueType.MAINT_REQD],
            ["EQUIP_DAMAGED", IssueType.EQUIP_DAMAGED],
            ["equip_damaged", IssueType.EQUIP_DAMAGED]
        ]
        for x in range(len(oracle)):
            self.assertEqual(oracle[x][1], IssueType.from_str(oracle[x][0]))

    def test_invalid_str(self):
        with self.assertRaises(NotImplementedError):
            IssueType.from_str("Test")

    def test_none(self):
        with self.assertRaises(NotImplementedError):
            IssueType.from_str(None)

    def test_repr(self):
        self.assertEqual("Issue Type: EQUIP_DAMAGED", IssueType.EQUIP_DAMAGED.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("EQUIP_DAMAGED", str(IssueType.EQUIP_DAMAGED), "string representation not same")

if __name__ == '__main__':
    unittest.main()
