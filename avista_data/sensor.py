from avista_data import db


class Sensor(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    identifier = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(1024))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    data = db.relationship('DataPoint', backref='sensor', lazy='dynamic')

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name is None or name == "":
            raise Exception("name cannot be None or empty")
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, desc):
        if desc is None or desc == "":
            raise Exception("value cannot be None or empty")
        self.description = desc

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, ident):
        if ident is None:
            raise Exception("value cannot be None or empty")
        self.identifier = ident

    def add_data_point(self, point):
        if point is None or point in self.data:
            return
        self.data.append(point)

    def __repr__(self):
        return "Sensor: {} = {}".format(self.name, self.identifier)

    def __str__(self):
        return "Sensor: {} = {}".format(self.name, self.identifier)
