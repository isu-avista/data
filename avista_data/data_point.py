from avista_data import db


class DataPoint(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def get_value(self):
        return self.value

    def set_value(self, value):
        if not isinstance(value, float):
            raise Exception("value is not a float")
        self.value = value

    def __repr__(self):
        return "Data Point: {}".format(self.value)

    def __str__(self):
        return "Data Point: {}".format(self.value)
