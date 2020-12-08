from avista_data import db
from avista_data.role import Role
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """Representation of a Service User

    Attributes:
        **id (int)**: primary key for this User

        **first_name (str)**: User's first name

        **last_name (str)**: User's last name

        **email (str)**: User's email address

        **password_hash (str)**: hash of the User's password

        **role (:obj: `Role`)**: role assigned to this User
    """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    api_keys = db.relationship('ApiKey', backref='user', lazy='dynamic')

    def __init__(self, json=None, *args, **kwargs):
        """Creates a new instance of this class

        Args:
            **json (:obj: `JSON`)**: json representing an instance of the class (optional)

            __*args__: arguments to initialize attributes of the class

            __**kwargs__: arguments to initialize attributes of the class

        """
        super().__init__(*args, **kwargs)
        self.update(json)

    def update(self, json):
        """Updates this instance using the values from the provided json data

        Args:
            **json (:obj: `JSON`)**: json data providing new values for this class

        """
        if json is not None:
            self.set_first_name(json.get('first_name'))
            self.set_last_name(json.get('last_name'))
            self.set_email(json.get('email'))
            self.set_password(json.get('password'))
            self.set_role(Role.from_str(json.get('role')))
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_first_name(self):
        """First Name associated with this instance

        Returns:
            The first name of the user represented by this instance

        """
        return self.first_name

    def set_first_name(self, name):
        """Assigns the first name for this instance

        Args:
            **name (str)**: The new first name for this instance

        Raises:
            Exception, if the first name provided is None or the empty string

        """
        if name is None or name == "":
            raise Exception("first name cannot be None or empty")
        self.first_name = name
        db.session.commit()

    def get_last_name(self):
        """Last Name associated with this instance

        Returns:
            The last name of the user represented by this instance

        """
        return self.last_name

    def set_last_name(self, name):
        """Assigns the last name for this instance

        Args:
            **name (str)**: The new last name for this instance

        Raises:
            Exception, if the last name provided is None or the empty string

        """
        if name is None or name == "":
            raise Exception("last name cannot be None or empty")
        self.last_name = name
        db.session.commit()

    def get_email(self):
        """Email associated with this instance

        Returns:
            The email of the user represented by this instance

        """
        return self.email

    def set_email(self, email):
        """Assigns the email for this instance

        Args:
            **email (str)**: The new email for this instance

        Raises:
            Exception, if the email provided is None or the empty string

        """
        if email is None or email == "":
            raise Exception("email cannot be None or empty")
        self.email = email
        db.session.commit()

    def get_role(self):
        """Role associated with this instance

        Returns:
            The role of the user represented by this instance

        """
        return self.role

    def set_role(self, role):
        """Assigns the role for this instance

        Args:
            **role (:obj: `Role`)**: The new role for this instance

        Raises:
            Exception, if the role provided is None

        """
        if role is None:
            raise Exception("role cannot be none")
        self.role = role
        db.session.commit()

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None
        user = cls.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return None

        return user

    def set_password(self, password):
        """Assigns the new password for this user, which is hashed and stored

        Args:
            **password (str)**: The new password to be hashed and stored
        """
        self.password_hash = generate_password_hash(password)
        db.session.commit()

    def check_password(self, password):
        """Checks whether the provided password is the same as the original

        Attributes:
            **password (str)**: Password to be checked

        Returns:
            True if the provided password is the same as the original, False otherwise
        """
        return check_password_hash(self.password_hash, password)

    def add_api_key(self, key):
        """Adds the provided key to the set of api keys for this server

        Args:
            **key (:obj: `ApiKey`)**: the ApiKey to be added
        """
        if key is not None and key not in self.api_keys:
            self.api_keys.append(key)
            db.session.commit()

    def __repr__(self):
        """An unambiguous representation of Server"""
        return f"User: {self.email}"

    def __str__(self):
        """A readable representation of Server"""
        return f"User: {self.email}"

    def to_dict(self):
        """Constructs a dictionary representation of the Server

        Returns:
            Dictionary representation of this server containing all of its attributes data.
        """
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            role=str(self.role)
        )
