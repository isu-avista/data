import unittest
from avista_data.unit import Unit


class UnitTest(unittest.TestCase):

    def test_from_str(self):
        oracle = [
            ["Hz", Unit.Hz],
            ["J", Unit.J],
            ["Db", Unit.Db],
            ["F", Unit.F],
            ["C", Unit.C],
            ["kWh", Unit.kWh]
        ]
        for x in range(len(oracle)):
            self.assertEqual(oracle[x][1], Unit.from_str(oracle[x][0]))

    def test_invalid_str(self):
        with self.assertRaises(NotImplementedError):
            Unit.from_str("Test")

    def test_none(self):
        with self.assertRaises(NotImplementedError):
            Unit.from_str(None)

    def test_repr(self):
        self.assertEqual("Unit: Hz", Unit.Hz.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("Hz", str(Unit.Hz), "string representation not same")


if __name__ == '__main__':
    unittest.main()
