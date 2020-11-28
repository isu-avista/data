from avista_data import db


class DataPoint(db.Model):
    """"Representation of a measured value from a sensor

    Attributes:
        id (int): The primary key for each data point instance
        value (float): The measure value
        timestamp (int): The point at which the measurement occurred
        sensor_id (int): The id of the sensor which made the measurement

    """

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def __init__(self, json=None, *args, **kwargs):
        """Creates a new instance of this class

        Args:
            json (:obj: `JSON`): json representing an instance of the class (optional)
            args: arguments to initialize attributes of the class
            kwargs: arguments to initialize attributes of the class

        """
        super().__init__(*args, **kwargs)
        self.update(json)

    def update(self, json):
        """Updates this instance using the values from the provided json data

        Args:
            json (:obj: `JSON`): json data providing new values for this class

        """
        if json is not None:
            self.value = json.get('value')
            self.timestamp = json.get('timestamp')
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_value(self):
        """Returns the current value of this instance

        Returns:
            value of the instance
        """
        return self.value

    def set_value(self, value):
        """Assigns the value for this instance

        Args:
            value (float): The new value for this instance

        Raises:
            Exception, if the provided value is not a float
        """
        if not isinstance(value, float):
            raise Exception("value is not a float")
        self.value = value
        db.session.commit()

    def get_timestamp(self):
        """Returns the current timestamp of this instance

        Returns:
            timestamp of the instance
        """
        return self.timestamp

    def set_timestamp(self, ts):
        """Assigns the timestamp for this instance

        Args:
            ts (int): The new timestamp for this instance

        Raises:
            Exception, if the provided timestamp is not an int
        """
        if not isinstance(ts, int):
            raise Exception("timestamp is not an int")
        self.timestamp = ts
        db.session.commit()

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
            value=self.value,
            timestamp=self.timestamp
        )
