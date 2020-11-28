import unittest
from avista_data.role import Role


class RoleTest(unittest.TestCase):
    
    def test_from_str(self):
        oracle = [
            ["USER", Role.USER],
            ["user", Role.USER],
            ["User", Role.USER],
            ["TECHNICIAN", Role.TECHNICIAN],
            ["technician", Role.TECHNICIAN],
            ["Technician", Role.TECHNICIAN],
            ["MANAGER", Role.MANAGER],
            ["manager", Role.MANAGER],
            ["Manager", Role.MANAGER],
            ["ADMIN", Role.ADMIN],
            ["admin", Role.ADMIN],
            ["Admin", Role.ADMIN]
        ]
        for x in range(len(oracle)):
            self.assertEqual(oracle[x][1], Role.from_str(oracle[x][0]))

    def test_invalid_str(self):
        with self.assertRaises(NotImplementedError):
            Role.from_str("Test")

    def test_none(self):
        with self.assertRaises(NotImplementedError):
            Role.from_str(None)

    def test_repr(self):
        self.assertEqual("Role: USER", Role.USER.__repr__(), "repr not same")

    def test_str(self):
        self.assertEqual("USER", str(Role.USER), "string representation not same")


if __name__ == '__main__':
    unittest.main()
