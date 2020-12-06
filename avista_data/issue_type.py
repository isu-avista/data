from enum import Enum


class IssueType(Enum):
    """Enum representing the different types of issues identified"""

    MAINT_REQD = 1
    EQUIP_DAMAGED = 2

    def __repr__(self):
        """An unambiguous representation of IssueType"""
        return f"Issue Type: {self.name}"

    def __str__(self):
        """A readable representation of IssueType"""
        return f"{self.name}"

    @staticmethod
    def from_str(value):
        """Provides an instance of the IssueType for the given string.

        Args:
            **value (str)**: String representation of IssueType literal

        Returns:
            IssueType: literal of issue type

        Raises:
            NotImplementedError: If value is not a defined enum literal of IssueType
        """
        if value in ('MAINT_REQD', 'maint_reqd'):
            return IssueType.MAINT_REQD
        elif value in ('EQUIP_DAMAGED', 'equip_damaged'):
            return IssueType.EQUIP_DAMAGED
        else:
            raise NotImplementedError
