from avista_data import db


class Device(db.Model):
    """Representation of the device or service

    Attributes:
        id (int): Primary key of this instance
        name (str): Name of this instance
        description (str): Description of this instance
        location (str): Location of the monitored equipment
        sensors (list): List of sensors attached
        issues (list): List of issues identified

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    description = db.Column(db.String(2048), unique=True)
    location = db.Column(db.String(1024))
    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')
    sec_conf = db.relationship('SecurityConfig', uselist=False, backref='device')
    serv_conf = db.relationship('ServerConfig', uselist=False, backref='device')
    issues = db.relationship('Issue', backref='device', lazy='dynamic')

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
            self.name = json.get('name')
            self.description = json.get('description')
            self.location = json.get('location')
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
            name (str): The new name for this instance

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
             The description of the issue represented by this instance

        """
        return self.description

    def set_description(self, desc):
        """Assigns the description for this instance

        Args:
            desc (str): The new description for this instance

        Raises:
            Exception, if the description provided is None or the empty string

        """
        if desc is None or desc == "":
            raise Exception("description cannot be None or empty")
        self.description = desc
        db.session.commit()

    def get_location(self):
        """Location associated with this instance

        Returns:
             The location of the issue represented by this instance

        """
        return self.location

    def set_location(self, loc):
        """Assigns the location for this instance

        Args:
            loc (str): The new location for this instance

        Raises:
            Exception, if the location provided is None or the empty string

        """
        if loc is None or loc == "":
            raise Exception("location cannot be None or empty")
        self.location = loc
        db.session.commit()

    def set_sec_conf(self, conf):
        """Assigns the security config for this instance

        Args:
            conf (:obj: `SecurityConfig`): The new security config for this instance

        """
        if conf is None:
            return
        self.sec_conf = conf
        db.session.commit()

    def get_sec_conf(self):
        """SecurityConfig associated with this instance

        Returns:
             The security config of the issue represented by this instance

        """
        return self.sec_conf

    def set_serv_conf(self, conf):
        """Assigns the ServerConfig for this instance

        Args:
            conf (:obj: `ServerConfig`): The new server config for this instance

        """
        if conf is None:
            return
        self.serv_conf = conf
        db.session.commit()

    def get_serv_conf(self):
        """ServerConfig associated with this instance

        Returns:
             The server config of the issue represented by this instance

        """
        return self.serv_conf

    def add_issue(self, issue):
        """Adds the provided issue to this instance

        Args:
            issue (:obj: `Issue`): The new issue to be added to this instance

        """
        if issue is None:
            return
        self.issues.append(issue)
        db.session.commit()

    def add_sensor(self, sensor):
        """Adds the provided sensor to this instance

        Args:
            sensor (:obj: `Sensor`): The new sensor to be added to this instance

        """
        if sensor is None:
            return
        self.sensors.append(sensor)
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Device"""
        return f"Device: {self.name}"

    def __str__(self):
        """A readable representation of Device"""
        return f"Device: {self.name}"

    def to_dict(self):
        """Constructs a dictionary representation of the Device

        Returns:
            Dictionary representation of this device containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            location=self.location
        )
