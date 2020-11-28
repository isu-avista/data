from avista_data import db
from werkzeug.security import generate_password_hash, check_password_hash


class ApiKey(db.Model):
    """Representation of an API Key for use by a user or server

    Attributes:
        id (int): Primary key of this instance
        key_hash (str): Hashed value of this key
        description (str): Description of this key
        user_id (int): Primary key of the parent user
        server_id (int): Primary key of the parent server
    """

    id = db.Column(db.Integer, primary_key=True)
    key_hash = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))

    def __init__(self, json=None, *args, **kwargs):
        """Creates a new instance of this class

        Args:
            json (:obj: `JSON`): json representing an instance of the class (optional)
            args: arguments to initialize attributes of the class
            kwargs: arguments to initialize attributes of the class

        """
        super().__init__(*args, **kwargs)
        self.update(json)

    def update(self, json):
        """Updates this instance using the values from the provided json data

        Args:
            json (:obj: `JSON`): json data providing new values for this class

        """
        if json is not None:
            self.set_key(json.get('key'))
            self.description = json.get('description')
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def set_key(self, key):
        """Assigns the new value of this key, which is hashed and stored

        Args:
            key (str): The key to be hashed and stored
        """
        self.key_hash = generate_password_hash(key)
        db.session.commit()

    def check_key(self, key):
        """Checks whether the provided key is the same as the original

        Attributes:
            key (str): Key to be checked

        Returns:
            True if the provided key is the same as the original, False otherwise
        """
        return check_password_hash(self.key_hash, key)

    def get_description(self):
        """Returns the description associated with this key

        Returns:
            The currently assigned description of this key
        """
        return self.description

    def set_description(self, desc):
        """Assigns the value of the description of this key

        Args:
            desc (str): The new description for this key

        Raises:
            Exception, if the provided description is None or the empty string
        """
        if desc is None or desc == "":
            raise Exception("description cannot be None or empty")
        self.description = desc

    def __repr__(self):
        """An unambiguous representation of Server"""
        return f"API Key: {self.description}"

    def __str__(self):
        """A readable representation of Server"""
        return f"API Key: {self.description}"

    def to_dict(self):
        """Constructs a dictionary representation of the Api Key

        Returns:
            Dictionary representation of this api key containing all of its attributes data.
        """
        return dict(
            id=self.id,
            description=self.description
        )
