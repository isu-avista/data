from avista_data import db


class ServerConfig(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
    items = db.relationship('ConfigItem', backref='serv_conf', lazy='dynamic')

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name is None or name == "":
            raise Exception("name cannot be None or empty")
        self.name = name

    def __repr__(self):
        return "Server Config: {}".format(self.name)

    def __str__(self):
        return "Server Config: {}".format(self.name)
