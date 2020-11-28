# Avista-Data


## Description

This is the base data package upon which all other isu-avista projects rely.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)
4. [License](#license)

## Installation

To install this use the following command.

```
pip3 install git+ssh://git@github.com/isu-avista/data.git
```

## Usage

### Working with the database

Before working with the classes in this module, you will need to prepare your database. Use the following commands to work with the database.

To add a new database migration use the following command from the project root directory:

```
flask db migrate -m message
```

To upgrade a database to the most recent migration use the following command from the project root directory:

```
flask db upgrade
```

To downgrade the database to a previous migration use the following command from the project root directory

```
flask db downgrade
```

### Module Initialization

Once you have the database setup you will need a flask app in order to initialize the module.

The code for this would look something like...

```python
import os
import avista_data
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
avista_data.init(app)
```

The idea here is that you need some form of database configuration, provided through a configuration object
or environment variables. You can then create the flask app (i.e., `app = Flask(__name__)`). Finally, you can
then initialize the `avista_data` module using `avista_data.init(app)`. (Note: don't forget the imports)

### Using the classes

Currently the data model is quite small and comprised of the following classes:

* **ApiKey** - Represents the API Keys of Users or Servers connected
* **ConfigItem** - Represents a Configuration Item
* **DataPoint** - Represents a Measured Value from a particular point in time
* **Device** - Represents the device hosting the service
* **Issue** - Represents an issue affecting monitored equipment
* **IssueType** - Enum representing the type of issue
* **PinOut** - Represents a RPi GPIO connection point for a Sensor
* **Role** - Enum defining roles for users
* **SecurityConfig** - Security Configuration of a service 
* **Sensor** - Sensor connected to an IoT device
* **Server** - Server connected to a device
* **ServerConfig** - Configuration of the running service
* **Status** - Status of the running service
* **Unit** - Enum defining different units of measurement
* **User** - Represents a User of the Service

The relationships between these classes can be seen through a review of the design documentation
on the wiki. Each class is essentially operated using the following methods (common to each class):

* `__init__(json)` - constructs a new instance and optionally populates its attributes with values from the json representation
* `update(json)` - updates an object instance to the values stored in the json representation
* `to_dict()` - returns a dictionary containing the values of the attributes of the object instance
* `get_attr()` - returns the value of some attribute `attr`
* `set_attr(...)` - sets the value of some attribute `attr` to the provided value in the arguments additionally this will commit the change to the database

For examples of usage we suggest reviewing the unit tests in the `tests/` directory of the project. 

## Credits

This module was contributed by:

- Isaac D. Griffith

## License

[LICENSE](LICENSE)
