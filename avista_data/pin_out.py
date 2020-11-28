from avista_data import db


class PinOut(db.Model):
    """Represents the connection of a sensor to a RPi

    Attributes:
        id (int): Primary key
        var (str): Name of the pin to which the value will be referenced
        pin (int): The pin to which the lead from the sensor is connected
        sensor_id (int): primary key of the parent Sensor

    """

    id = db.Column(db.Integer, primary_key=True)
    var = db.Column(db.String(128), nullable=False)
    pin = db.Column(db.Integer, nullable=False)
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
            self.var = json.get('var')
            self.pin = json.get('pin')
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_var(self):
        """Returns the current var name of the current instance

        Returns:
            the instance's current var name

        """
        return self.var

    def set_var(self, var):
        """Assigns the current instance the provided pin name

        Args:
            var (str): new var name of the pin to which the sensor is attached

        Raises:
            Exception, if var is none or empty string
        """
        if var is None or var == "":
            raise Exception('var cannot be None or Empty')
        self.var = var
        db.session.commit()

    def get_pin(self):
        """Returns the current pin of the current instance

        Returns:
            the instance's current pin

        """
        return self.pin

    def set_pin(self, pin):
        """Assigns the current instance the provided pin

        Args:
            pin (int): new pin to which the sensor is attached

        Raises:
            Exception, if pin is none or less than 1 or greater than 40
        """
        if pin is None or pin < 1 or pin > 40:
            raise Exception('pin value cannot be none, less than 1 or greater than 40')
        self.pin = pin
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Server"""
        return f"Pin Out: <{self.var}, {self.pin}>"

    def __str__(self):
        """A readable representation of Server"""
        return f"Pin Out: <{self.var}, {self.pin}>"

    def to_dict(self):
        """Constructs a dictionary representation of the pinout

        Returns:
            Dictionary representation of this pinout containing all of its attributes data.
        """
        return dict(
            id=self.id,
            var=self.var,
            pin=self.pin
        )
