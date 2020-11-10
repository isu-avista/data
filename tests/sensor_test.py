import unittest
from tests.base_test import BaseTest
from avista_data.sensor import Sensor


class SensorTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.fixture = Sensor()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
