from avista_data import db
from avista_data.issue_type import IssueType


class Issue(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    type = db.Column(db.Enum(IssueType), nullable=False)
