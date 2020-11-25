from avista_data import db
from avista_data.unit import Unit


class DataPoint(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Enum(Unit), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def get_value(self):
        return self.value

    def set_value(self, value):
        if not isinstance(value, float):
            raise Exception("value is not a float")
        self.value = value

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        if not isinstance(timestamp, int):
            raise Exception("timestamp is not an int")
        self.timestamp = timestamp

    def get_unit(self):
        return self.unit

    def set_unit(self, unit):
        if unit is None:
            raise Exception("Unit cannot be none")
        self.unit = unit

    def __repr__(self):
        return "Data Point: {}".format(self.value)

    def __str__(self):
        return "Data Point: {}".format(self.value)
