from avista_data import db


class Device(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    description = db.Column(db.String(2048))
    location = db.Column(db.String(1024))
    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')
    sec_conf = db.relationship('SecurityConfig', backref='device', lazy='dynamic')
    serv_conf = db.relationship('ServerConfig', backref='device', lazy='dynamic')
    issues = db.relationship('Issue', backref='device', lazy='dynamic')

    def __repr__(self):
        return "Device: {}".format(self.name)

    def __str__(self):
        return "Device: {}".format(self.name)
