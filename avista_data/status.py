from avista_data import db


class Status(db.Model):
    """Representation of items representing the current status of the device/service

    Attributes:
        **id (int)**: Primary key

        **name (str)**: Name of the status item being observed

        **value (int)**: Value of the item (0, 1, 2) - (Good, Warning, Danger)

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

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
            self.set_name(json.get('name'))
            self.set_value(json.get('value'))
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_name(self):
        """Name associated with this instance

        Returns:
            The name of the server represented by this instance

        """
        return self.name

    def set_name(self, name):
        """Assigns the name for this instance

        Args:
            **name (str)**: The new name for this instance

        Raises:
            Exception, if the name provided is None or the empty string

        """
        if name is None or name == "":
            raise Exception('name cannot be None or Empty')
        self.name = name
        db.session.commit()

    def get_value(self):
        """Value associated with this instance

        Returns:
            The value of the server represented by this instance

        """
        return self.value

    def set_value(self, value):
        """Assigns the value for this instance

        Args:
            **value (int)**: The new value for this instance

        Raises:
            Exception, if the value provided is None or outside the range 0 <= value <= 3

        """
        if value is None or value < 0 or value > 3:
            raise Exception('value cannot be None or less than 0 or greater than 3')
        self.value = value
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Server"""
        return f"Status: {self.name} = {self.value}"

    def __str__(self):
        """A readable representation of Server"""
        return f"Status: {self.name} = {self.value}"

    def to_dict(self):
        """Constructs a dictionary representation of the Server

        Returns:
            Dictionary representation of this server containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            value=self.value
        )
