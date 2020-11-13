from enum import Enum


class Unit(Enum):
    """Enum representing the different types of units produced for values from the sensors"""

    HZ = 1
    J = 2
    DB = 3
    F = 4
    C = 5
    KWH = 6

    def __repr__(self):
        return "Unit: {}".format(self.name)

    def __str__(self):
        return "Unit: {}".format(self.name)
