from enum import Enum


class Unit(Enum):
    """Enum representing the different types of units produced for values from the sensors"""

    Hz = 1
    J = 2
    Db = 3
    F = 4
    C = 5
    kWh = 6

    def __repr__(self):
        """An unambiguous representation of Unit"""
        return f"Unit: {self.name}"

    def __str__(self):
        """A readable representation of Unit"""
        return f"{self.name}"

    @staticmethod
    def from_str(label):
        """Provides an instance of the IssueType for the given string.

        Args:
            **label (str)**: String representation of Unit literal

        Returns:
            Unit: literal of unit

        Raises:
            NotImplementedError: If value is not a defined enum literal of Unit
        """
        if label == 'Hz':
            return Unit.Hz
        elif label == 'J':
            return Unit.J
        elif label == 'Db':
            return Unit.Db
        elif label == 'F':
            return Unit.F
        elif label == 'C':
            return Unit.C
        elif label == 'kWh':
            return Unit.kWh
        else:
            raise NotImplementedError
