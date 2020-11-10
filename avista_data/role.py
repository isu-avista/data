from enum import Enum


class Role(Enum):
    """ """

    USER = 1
    TECHNICIAN = 2
    MANAGER = 3
    ADMIN = 4

    def __repr__(self):
        return "Role: {}".format(self.value)

    def __str__(self):
        return "Role: {}".format(self.value)