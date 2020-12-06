from avista_data import db


class SecurityConfig(db.Model):
    """A representation of the security configuration for a given Server

    Attributes:
        **id (int)**: primary key of this instance

        **name (str)**: Name of this configuration

        **device_id (int)**: Device to which this configuration belongs

        **items (list)**: List of configuration items associated with this configuration

        **items (list)**: List of users associated with this configuration
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
    items = db.relationship('ConfigItem', backref='sec_conf', lazy='dynamic')

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
            raise Exception("name cannot be None or empty")
        self.name = name
        db.session.commit()

    def add_item(self, item):
        """Adds the provided config item to this configuration

        Args:
            **item (:obj: `ConfigItem`)**: The item to be added
        """
        if item is None or item in self.items:
            return
        self.items.append(item)
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Configuration"""
        return f"Security Config: {self.name}"

    def __str__(self):
        """A readable representation of Configuration"""
        return f"Security Config: {self.name}"

    def to_dict(self):
        """Constructs a dictionary representation of the configuration

        Returns:
            Dictionary representation of this config containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
        )
