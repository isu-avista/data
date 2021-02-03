from avista_data import db


class ConfigItem(db.Model):
    """Representation of a single item from a configuration

    Attributes:
        **id (int)**: The primary key for each config item instance

        **name (str)**: Name of this instance

        **description (str)**: Description of this instance

        **value (str)**: Config value

        **sec_conf_id (int)**: primary key of containing security configuration

        **serv_conf_id (int)**; primary key of containing server configuration
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String(2048), unique=True, nullable=False)
    value = db.Column(db.String(1024), nullable=False)
    sec_conf_id = db.Column(db.Integer, db.ForeignKey('security_config.id'))
    serv_conf_id = db.Column(db.Integer, db.ForeignKey('server_config.id'))

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
            self.description = json.get('description')
            self.value = (json.get('value'))
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
            The name of the config item represented by this instance

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

    def get_description(self):
        """Description associated with this instance

        Returns:
            The description of the config item represented by this instance

        """
        return self.description

    def set_description(self, desc):
        """Assigns the description for this instance

        Args:
            **desc (str)**: The new description for this instance

        Raises:
            Exception, if the description provided is None or the empty string

        """
        if desc is None or desc == "":
            raise Exception("description cannot be None or empty")
        self.description = desc
        db.session.commit()

    def get_value(self):
        """Returns the current value of this instance

        Returns:
            value of the instance
        """
        return self.value

    def set_value(self, value):
        """Assigns the value for this instance

        Args:
            **value (str)**: The new value for this instance

        Raises:
            Exception, if the provided value is not a float
        """
        if value is None or value == "":
            raise Exception("value cannot be None or empty")
        self.value = value
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of ConfigItem"""
        return f"Config Item: {self.name}={self.value}"

    def __str__(self):
        """A readable representation of ConfigItem"""
        return f"Config Item: {self.name}={self.value}"

    def to_dict(self):
        """Constructs a dictionary representation of the ConfigItem

        Returns:
            Dictionary representation of this config item containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            value=self.value,
        )
