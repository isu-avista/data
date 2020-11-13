from avista_data import db


class Device(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    description = db.Column(db.String(2048), unique=True)
    location = db.Column(db.String(1024))
    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')
    sec_conf = db.relationship('SecurityConfig', uselist=False, backref='device')
    serv_conf = db.relationship('ServerConfig', uselist=False, backref='device')
    issues = db.relationship('Issue', backref='device', lazy='dynamic')

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
            raise Exception("description cannot be None or empty")
        self.description = desc

    def get_location(self):
        return self.location

    def set_location(self, loc):
        if loc is None or loc == "":
            raise Exception("location cannot be None or empty")
        self.location = loc

    def set_sec_conf(self, conf):
        if conf is None:
            return
        self.sec_conf = conf

    def get_sec_conf(self):
        return self.sec_conf

    def set_serv_conf(self, conf):
        if conf is None:
            return
        self.serv_conf = conf

    def get_serv_conf(self):
        return self.serv_conf

    def add_issue(self, issue):
        if issue is None:
            return
        self.issues.append(issue)

    def add_sensor(self, sensor):
        if sensor is None:
            return
        self.sensors.append(sensor)

    def __repr__(self):
        return "Device: {}".format(self.name)

    def __str__(self):
        return "Device: {}".format(self.name)
