from avista_data import db


class DataPoint(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def __repr__(self):
        return "Data Point: {}".format(self.value)

    def __str__(self):
        return "Data Point: {}".format(self.value)
