from avista_data import db


class ConfigItem(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String(2048), unique=True, nullable=False)
    value = db.Column(db.String(1024), nullable=False)
    sec_conf_id = db.Column(db.Integer, db.ForeignKey('security_config.id'))
    serv_conf_id = db.Column(db.Integer, db.ForeignKey('server_config.id'))

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

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value is None or value == "":
            raise Exception("value cannot be None or empty")
        self.value = value

    def __repr__(self):
        return "Config Item: {}={}".format(self.name, self.value)

    def __str__(self):
        return "Config Item: {}={}".format(self.name, self.value)
