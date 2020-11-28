from enum import Enum


class Role(Enum):
    """Enum representing the different roles for users"""

    USER = 1
    TECHNICIAN = 2
    MANAGER = 3
    ADMIN = 4

    def __repr__(self):
        """An unambiguous representation of Role"""
        return f"Role: {self.name}"

    def __str__(self):
        """A readable representation of Role"""
        return f"{self.name}"

    @staticmethod
    def from_str(label):
        """Provides an instance of the Role for the given string.

        Args:
            label (str): String representation of Role literal

        Returns:
            Role: literal of role

        Raises:
            NotImplementedError: If value is not a defined enum literal of Role
        """
        if label in ('USER', 'user', 'User'):
            return Role.USER
        elif label in ('TECHNICIAN', 'technician', 'Technician'):
            return Role.TECHNICIAN
        elif label in ('MANAGER', 'manager', 'Manager'):
            return Role.MANAGER
        elif label in ('ADMIN', 'admin', 'Admin'):
            return Role.ADMIN
        else:
            raise NotImplementedError
