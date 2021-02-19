from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Parameter(Base):
    """Represents parameters that can be used by Sensors

    Attributes:
        **id (int)**: Primary key

        **key (str)**: The parameter key

        **value (str)**: The parameter value

        **sensor_id (int)**: Primary key of the parent Sensor

    """

    __tablename__ = "Parameters"
    id = Column(Integer, primary_key=True)
    key = Column(String(128), nullable=False)
    value = Column(String(128), nullable=False)
    sensor_id = Column(Integer, ForeignKey('Sensors.id'))

    def __init__(self, json=None, *args, **kwargs):
        """Creates a new instance of this class

        Args:
            **json (:obj: `JSON`)**: json representing an instance of the class (optional)

            __*args__: arguments to initialize attributes of the class

            __**kwargs__: arguments to initialize attributes of the class
        """
        super().__init__(*args, **kwargs)
        self.update(json)

    def update(self, json):
        """Updates this instance using the values from the provided json data

        Args:
            **json (:obj: `JSON`)**: json data providing new values for this class

        """
        if json is not None:
            self.key = json.get('key')
            self.value = json.get('value')

    def get_id(self):
        """Gets the primary key of this instance

        Returns:
            the primary key id of this instance

        """
        return self.id

    def get_key(self):
        """Gets the key of this instance

        Returns:
            the key of this instance

        """
        return self.key

    def set_key(self, key):
        """Assigns the current instance the provided key

        Args:
            **key (str)**: the new key for this instance

        Raises:
            Exception, if key is None or Empty

        """
        if key is None or key == "":
            raise Exception('key cannot be None or Empty')
        self.key = key

    def get_value(self):
        """Gets the value of this instance

        Returns:
            the value of this instance

        """
        return self.value

    def set_value(self, value):
        """Assigns the current instance the provided value

        Args:
            **value (str)**: the new value for this instance

        Raises:
            Exception, if value is None or Empty

        """
        if value is None or value == "":
            raise Exception('value cannot be None or Empty')
        self.value = value

    def __repr__(self):
        """An unambiguous representation of a Parameter"""
        return f"Parameter: [{self.key}] = {self.value}"

    def __str__(self):
        """A readable representation of a Parameter"""
        return f"Parameter: [{self.key}] = {self.value}"

    def to_dict(self):
        """Constructs a dictionary representation of the current Parameter

        Returns:
            dictionary representation of this Parameter containing all of its attributes

        """
        return dict(
            id=self.id,
            key=self.key,
            value=self.value
        )
