from avista_data import db


class ConfigItem(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    description = db.Column(db.String(2048), index=True, unique=True)
    value = db.Column(db.String(1024))
    sec_conf_id = db.Column(db.Integer, db.ForeignKey('security_config.id'))
    serv_conf_id = db.Column(db.Integer, db.ForeignKey('server_config.id'))

    def __repr__(self):
        return "Config Item: {}={}".format(self.name, self.value)

    def __str__(self):
        return "Config Item: {}={}".format(self.name, self.value)
