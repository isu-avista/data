from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class DataPoint(Base):
    """"Representation of a measured value from a sensor

    Attributes:
        **id (int)**: The primary key for each data point instance

        **value (float)**: The measure value

        **name (str)**: The name of the datapoint

        **timestamp (int)**: The point at which the measurement occurred

        **sensor_id (int)**: The id of the sensor which made the measurement

    """
    __tablename__ = "DataPoints"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)
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
            self.name = json.get('name')
            self.value = json.get('value')
            self.timestamp = json.get('timestamp')

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_name(self):
        """Returns the current name of this instance

        Returns:
            name of the instance
        """
        return self.name

    def set_name(self, name):
        """Assigns the name for this instance

        Args:
            **name (str)**: The new name for this instance

        Raises:
            Exception, if the provided name is not a string
        """
        if not isinstance(name, str):
            raise Exception("name is not a string")
        self.name = name

    def get_value(self):
        """Returns the current value of this instance

        Returns:
            value of the instance
        """
        return self.value

    def set_value(self, value):
        """Assigns the value for this instance

        Args:
            **value (float)**: The new value for this instance

        Raises:
            Exception, if the provided value is not a float
        """
        if not isinstance(value, float):
            raise Exception("value is not a float")
        self.value = value

    def get_timestamp(self):
        """Returns the current timestamp of this instance

        Returns:
            timestamp of the instance
        """
        return self.timestamp

    def set_timestamp(self, ts):
        """Assigns the timestamp for this instance

        Args:
            **ts (int)**: The new timestamp for this instance

        Raises:
            Exception, if the provided timestamp is not an int
        """
        if not isinstance(ts, int):
            raise Exception("timestamp is not an int")
        self.timestamp = ts

    def __repr__(self):
        """An unambiguous representation of DataPoint"""
        return f"Data Point: {self.value}"

    def __str__(self):
        """A readable representation of DataPoint"""
        return f"Data Point: {self.value}"

    def to_dict(self):
        """Constructs a dictionary representation of the DataPoint

        Returns:
            Dictionary representation of this data point containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            value=self.value,
            timestamp=self.timestamp
        )
