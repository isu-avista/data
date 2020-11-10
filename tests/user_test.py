import unittest
from tests.base_test import BaseTest


class MyTestCase(BaseTest):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
