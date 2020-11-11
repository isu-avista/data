from avista_data import db
from avista_data.issue_type import IssueType


class Issue(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    type = db.Column(db.Enum(IssueType), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

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

    def get_type(self):
        return self.type

    def set_type(self, type):
        if type is None:
            raise Exception("value cannot be None or empty")
        self.type = type

    def __repr__(self):
        return "Issue: {}".format(self.name)

    def __str__(self):
        return "Issue: {}".format(self.name)