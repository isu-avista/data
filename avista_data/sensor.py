from avista_data import db


class Sensor(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, index=True)
    identifier = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(1024))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    data = db.relationship('DataPoint', backref='sensor', lazy='dynamic')

    def __repr__(self):
        return "Sensor: {} = {}".format(self.name, self.identifier)

    def __str__(self):
        return "Sensor: {} = {}".format(self.name, self.identifier)
