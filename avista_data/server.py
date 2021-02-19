import re

import avista_data
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Server(Base):
    """A representation of servers to which the device is connected and to which data will be provided

    Attributes:
        **id (int)**: The primary key for each server connected

        **name (str)**: The name of the server

        **ip_address (str)**: The ip address of the server

        **port (int)**: The port of the server to which data is to be sent

        **periodicity (int)**: The time in milliseconds between data updates to the server

        **api_keys (list)**: The api keys associated with this server

    """

    __tablename__ = "Servers"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    ip_address = Column(String(128))
    port = Column(Integer)
    periodicity = Column(Integer)
    api_keys = relationship('ApiKey', backref='server', lazy='dynamic')
    device_id = Column(Integer, ForeignKey('Devices.id'))

    def __init__(self, json=None, *args, **kwargs):
        """Creates a new instance of this class

        Args:
            **json (:obj: `JSON`)**: json representing an instance of the class (optional)

            __*args__: arguments to initialize attributes of the class

            __**kwargs__: arguments to initialize attributes of the class

        """
        super().__init__(*args, **kwargs)
        self.db = avista_data.database.db
        self.db.add(self)
        self.update(json)

    def update(self, json):
        """Updates this instance using the values from the provided json data

        Args:
            **json (:obj: `JSON`)**: json data providing new values for this class

        """
        if json is not None:
            self.set_name(json.get('name'))
            self.set_ip_address(json.get('ip_address'))
            self.set_port(int(json.get('port')))
            self.set_periodicity(int(json.get('periodicity')))
            self.db.commit()

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
            **name (str)**: The new name for this instance

        Raises:
            Exception, if the name provided is None or the empty string

        """
        if name is None or name == "":
            raise Exception("name cannot be None or empty")
        self.name = name
        # self.db.commit()

    def get_ip_address(self):
        """Returns the current ip address of this instance

        Returns:
            instance ip address
        """
        return self.ip_address

    def set_ip_address(self, ip):
        """Assigns the ip address for this instance

        Args:
            **ip (str)**: The new ip address for this instance

        Raises:
            Exception, if the ip address provide is None, the empty string, or improperly formatted

        """
        if ip is None or ip == "":
            raise Exception("ip cannot be None or empty")
        match = re.search("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                          ip)
        if match is None:
            raise Exception("ip is not properly formatted")
        self.ip_address = ip
        # self.db.commit()

    def get_port(self):
        """Returns the current port of this instance

        Returns:
            port of the instance
        """
        return self.port

    def set_port(self, port):
        """Assigns the port for this instance

        Args:
            **port (int)**: The new port for this instance

        Raises:
            Exception, if the provided port is None, or outside the range 0 < port < 65536
        """
        if port is None or port < 1 or port > 65535:
            raise Exception("port cannot be None or less than 1 or greater than 65535")
        self.port = port
        # self.db.commit()

    def get_periodicity(self):
        """Returns the current periodicity of the current instance

        Returns:
            the instance's current data update periodicity in milliseconds

        """
        return self.periodicity

    def set_periodicity(self, period):
        """Assigns the current instance the provided update periodicity in milliseconds

        Args:
           ** period (int)**: new periodicity in milliseconds

        Raises:
            Exception, if period is none or less than or equal to 0
        """
        if period is None or period <= 0:
            raise Exception("periodicity cannot be None or less than 1")
        self.periodicity = period
        # self.db.commit()

    def add_api_key(self, key):
        """Adds the provided key to the set of api keys for this server

        Args:
            **key (:obj: `ApiKey`)**: the ApiKey to be added
        """
        if key is not None and key not in self.api_keys:
            self.api_keys.append(key)
            # self.db.commit()

    def __repr__(self):
        """An unambiguous representation of Server"""
        return f"Server: {self.name}"

    def __str__(self):
        """A readable representation of Server"""
        return f"Server: {self.name}"

    def to_dict(self):
        """Constructs a dictionary representation of the Server

        Returns:
            Dictionary representation of this server containing all of its attributes data.
        """
        return dict(
            id=self.id,
            name=self.name,
            ip_address=self.ip_address,
            port=self.port,
            periodicity=self.periodicity
        )
