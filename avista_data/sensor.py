from avista_data import db
from avista_data.unit import Unit
from avista_data.parameter import Parameter


class Sensor(db.Model):
    """Class representing an attached sensor.

    This allows for the dynamic construction and removal of sensors from the device

    Attributes:
        **id (int)**: The primary key for this sensor

        **name (str)**: The name of this sensor

        **quantity (str)**: The measured quantity

        **unit (:obj: `Unit`)**: The units of measurement

        **module (str)**: The module

        **cls (str)**: The class name of the sensor to be used

        **data (list)**: List of data points measured by the sensor

        **parameters (list)**: List of parameters used by the sensor

        **device_id (int)**: id of the parent device to which this sensor is attached

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    quantity = db.Column(db.String(128))
    unit = db.Column(db.Enum(Unit))
    module = db.Column(db.String(1024))
    cls = db.Column(db.String(1024))
    data = db.relationship('DataPoint', backref='sensor', lazy='dynamic')
    parameters = db.relationship('Parameter', backref='sensor', lazy='dynamic')
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
            self.name = json.get('name')
            self.quantity = json.get('quantity')
            self.unit = Unit.from_str(json.get('unit'))
            self.cls = json.get('cls')
            self.module = json.get('module')
            for p in json.get('parameters'):
                self.add_parameter(Parameter(p))
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
            The name of the sensor represented by this instance

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

    def get_quantity(self):
        """The quantity to be measured by this sensor

        Returns:
            Current quantity measured
        """
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity to be measured by the sensor

        Args:
            **quantity (str)**: The new quantity to be measured

        Raises:
            Exception, if the provided quantity is None or empty
        """
        if quantity is None or quantity == "":
            raise Exception("quantity cannot be None or empty")
        self.quantity = quantity
        db.session.commit()

    def add_data_point(self, point):
        """Adds the provided data point as a measure of this sensor

        Args:
            **point (:obj: `DataPoint`)**: DataPoint measured

        """
        if point is None or point in self.data:
            return
        self.data.append(point)
        db.session.commit()

    def add_parameter(self, parameter):
        """Adds the provided parameter to this sensor

        Args:
            **parameter (:obj: `Parameter`)**: Parameter to be added

        """
        if parameter is None or parameter in self.parameters:
            return
        self.parameters.append(parameter)
        db.session.commit()

    def get_unit(self):
        """Returns the unit of measure associated with this sensor

        Returns:
            The unit of measure of this sensor

        """
        return self.unit

    def set_unit(self, unit):
        """Sets the unit of measurement for the sensor

        Args:
            **unit (:obj: `Unit`)**: New unit for the sensor

        Raises:
            Exception if the provided unit is None

        """
        if unit is None:
            raise Exception("Unit cannot be none")
        self.unit = unit
        db.session.commit()

    def get_class(self):
        """Returns the class used by this instance"""
        return self.cls

    def set_class(self, cls):
        """Sets the class used by this instance to the string provided

        Args:
            **cls (str)**: The class to be used

        Raises:
            Exception, if either the provided string is None or empty

        """
        if cls is None or cls == "":
            raise Exception("cls cannot be None or empty")
        self.cls = cls
        db.session.commit()

    def get_module(self):
        """Returns the module used by this instance"""
        return self.module

    def set_module(self, module):
        """Sets the module used by this instance to the string provided

        Args:
            **module (str)**: The module to be used

        Raises:
            Exception, if either the provided string is None or empty

        """
        if module is None or module == "":
            raise Exception("module cannot be None or empty")
        self.module = module
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Sensor"""
        return f"Sensor: {self.name} = {self.quantity}"

    def __str__(self):
        """A readable representation of Sensor"""
        return f"Sensor: {self.name} = {self.quantity}"

    def to_dict(self):
        """Constructs a dictionary representation of the Sensor

        Returns:
            Dictionary representation of this sensor containing all of its attributes data.

        """
        parameters = []
        for p in Parameter.query.with_parent(self).all():
            parameters.append(p.to_dict())
        return dict(
            id=self.id,
            name=self.name,
            quantity=self.quantity,
            cls=self.cls,
            module=self.module,
            parameters=parameters,
            unit=str(self.unit),
        )
