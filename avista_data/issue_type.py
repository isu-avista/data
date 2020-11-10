from enum import Enum


class IssueType(Enum):
    """Enum representing the different types of issues identified"""

    MAINT_REQD = 1
    EQUIP_DAMAGED = 2

    def __repr__(self):
        return "Issue Type: {}".format(self.value)

    def __str__(self):
        return "Issue Type: {}".format(self.value)