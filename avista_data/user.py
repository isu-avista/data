from avista_data import db
from avista_data import role
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """ """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(32), unique=True)
    role = db.Column(db.Enum(role.Role), nullable=False)

    def __repr__(self):
        return "User: {}".format(self.email)

    def __str__(self):
        return "User: {}".format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
