from avista_data import db


class SecurityConfig(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, index=True)
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
    items = db.relationship('ConfigItem', backref='sec_conf', lazy='dynamic')
    users = db.relationship('Users', backref='config', lazy='dynamic')

    def __repr__(self):
        return "Security Config: {}".format(self.name)

    def __str__(self):
        return "Security Config: {}".format(self.name)
