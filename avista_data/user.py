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
    sec_conf_id = db.Column(db.Integer, db.ForeignKey('security_config.id'))

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, name):
        if name is None or name == "":
            raise Exception("first name cannot be None or empty")
        self.first_name = name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, name):
        if name is None or name == "":
            raise Exception("last name cannot be None or empty")
        self.last_name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if email is None or email == "":
            raise Exception("email cannot be None or empty")
        self.email = email

    def get_role(self):
        return self.role

    def set_role(self, role):
        if role is None:
            raise Exception("role cannot be none")
        self.role = role

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "User: {}".format(self.email)

    def __str__(self):
        return "User: {}".format(self.email)
