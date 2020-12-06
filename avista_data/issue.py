from avista_data import db
from avista_data.issue_type import IssueType


class Issue(db.Model):
    """Represents an issue associated with the measured equipment

    Attributes:
        **id (int)**: The primary key for this issue<br/>
        name (str): Name associated with this issue<br/>
        description (str): Description associated with this issue<br/>
        type (:obj: IssueType): Type associated with this issue<br/>
        device_id (int): Primary key of the device to which this issue is associated

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    type = db.Column(db.Enum(IssueType), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

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
            self.name = json.get('name')
            self.description = json.get('description')
            self.type = IssueType.from_str(json.get('type'))
            db.session.commit()

    def get_id(self):
        """Primary key of this instance

        Returns:
            the primary key id of this instance
        """
        return self.id

    def get_name(self):
        """Name associated with this instance

        Returns:
             The name of the server represented by this instance

        """
        return self.name

    def set_name(self, name):
        """Assigns the name for this instance

        Args:
            name (str): The new name for this instance

        Raises:
            Exception, if the name provided is None or the empty string

        """
        if name is None or name == "":
            raise Exception("name cannot be None or empty")
        self.name = name
        db.session.commit()

    def get_description(self):
        """Description associated with this instance

        Returns:
             The description of the issue represented by this instance

        """
        return self.description

    def set_description(self, desc):
        """Assigns the description for this instance

        Args:
            desc (str): The new description for this instance

        Raises:
            Exception, if the description provided is None or the empty string

        """
        if desc is None or desc == "":
            raise Exception("value cannot be None or empty")
        self.description = desc
        db.session.commit()

    def get_type(self):
        """IssueType associated with this instance

        Returns:
             The type of the issue represented by this instance

        """
        return self.type

    def set_type(self, new_type):
        """Assigns the IssueType for this instance

        Args:
            new_type (:obj: `IssueType`): The new type for this instance

        Raises:
            Exception, if the issue type provided is None

        """
        if new_type is None:
            raise Exception("value cannot be None or empty")
        self.type = new_type
        db.session.commit()

    def __repr__(self):
        """An unambiguous representation of this Issue"""
        return f"Issue: {self.name}"

    def __str__(self):
        """A readable representation of this Issue"""
        return f"Issue: {self.name}"

    def to_dict(self):
        """Constructs a dictionary representation of the Issue

        Returns:
            Dictionary representation of this issue containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            type=str(self.type)
        )
