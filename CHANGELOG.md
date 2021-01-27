# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

### Deleted

## [1.1.0](https://github.com/isu-avista/data/releases/tag/v1.1.0) - 2021-01-27
### Added
* Added a parameter class to store parameters for use with sensors at runtime

### Changed

### Deleted

## [1.0.0](https://github.com/isu-avista/data/releases/tag/v1.0.0) - 2021-01-17
### Added
* Added channel attribute to the sensor class

### Changed

### Deleted
* Removed the pinout class and pinout associations inside the sensor class

## [0.1.17](https://github.com/isu-avista/data/releases/tag/v0.1.17) - 2020-12-15
### Added

### Changed
* Refactored db.create_all() to be in proper place in `populate_initial_data()`

### Deleted

## [0.1.16](https://github.com/isu-avista/data/releases/tag/v0.1.16) - 2020-12-13
### Added

### Changed
* Updated Changelog

### Deleted

## [0.1.15](https://github.com/isu-avista/data/releases/tag/v0.1.15) - 2020-12-13
### Added
* New class to better manage integration with flask via flask constructs

### Changed
* Updated documentation
* Added method to User to reset the admin user
* Updated user test to include tests for the new methods 
* Updated base test to use the new data manager
* Updated the User class to allow initialization of data in the database

### Deleted

## [0.1.14](https://github.com/isu-avista/data/releases/tag/v0.1.14) - 2020-12-08
### Added

### Changed
* Updated documentation

### Deleted

## [0.1.13](https://github.com/isu-avista/data/releases/tag/v0.1.13) - 2020-12-11
### Added

### Changed
- Minor adjustment to Server.port validation code

### Deleted

## [0.1.12](https://github.com/isu-avista/data/releases/tag/v0.1.12) - 2020-12-08
### Added

### Changed
- Added tests to ensure authenticate() method works.

### Deleted

## [0.1.11](https://github.com/isu-avista/data/releases/tag/v0.1.11) - 2020-12-08
### Added

### Changed
- Modified parameters to User.authenticate() method

### Deleted

## [0.1.10](https://github.com/isu-avista/data/releases/tag/v0.1.10) - 2020-12-08
### Added

### Changed
- Added code to create admin user if none exist
- Update documentation

### Deleted

## [0.1.9](https://github.com/isu-avista/data/releases/tag/v0.1.9) - 2020-12-07
### Added
- RoleTooLowError to distinguish when a user with too low of permissions
  attempts to access something they are not authorized to

### Changed
- Updated Role to an IntEnum to allow for comparisons
- Updated Tests
- Updated Documentation

### Deleted

## [0.1.8](https://github.com/isu-avista/data/releases/tag/v0.1.8) - 2020-12-05
### Added

### Changed
- Cleaned up the sphinx documentation in all classes

### Deleted

## [0.1.7](https://github.com/isu-avista/data/releases/tag/v0.1.7) - 2020-12-05
### Added

### Changed
- Updated readme to point to key project wikis
- Added license information directly to the readme
- Updated the changelog to link to the actual releases

### Deleted

## [0.1.6](https://github.com/isu-avista/data/releases/tag/v0.1.6) - 2020-12-03
### Added
- Added module field to Sensor
- Added migration

### Changed

### Deleted

## [0.1.5](https://github.com/isu-avista/data/releases/tag/v0.1.5) - 2020-11-28
### Added
- Added github page documentation to the project
- Modified the README to provide instructions for generating documentation
- New migrations to ensure the db is correct

### Changed
- Modified several classes to ensure the relationships are correct according to the design

### Removed
- All old migrations

## [0.1.4](https://github.com/isu-avista/data/releases/tag/v0.1.4) - 2020-11-28
### Added
- New migration for the changes to Sensor and Datapoint
- Quantity field to Sensor
- New migration for changes to sensor
- New class representing sensor pinouts
- New class representing attached servers
- New class representing service status
- to_dict() method to each class
- update() method to each class
- New Migration for adding api keys
- New class representing api keys and connected it to both servers and users

### Changed
- Added unit to Sensor and removed it from Datapoint
- Updated all tests to reflect changes (100% Line Coverage)
- Updated the documentation for all of the classes
- All set_xxx() methods now automatically commit to the database
- Updated the README.md to include Usage information

### Removed
- Description field from Sensor
- Identifier field from Sensor

## [0.1.3](https://github.com/isu-avista/data/releases/tag/v0.1.3) - 2020-11-25
### Added
- New migration for datapoint

### Changed
- Added a new field to Datapoint to incorporate the timestamp of the data

### Removed
- Nothing

## [0.1.2](https://github.com/isu-avista/data/releases/tag/v0.1.2) - 2020-11-13
### Added
- Nothing

### Changed
- Updated setup.py to accurately reflect the module name and version

### Removed
- Nothing

## [0.1.1](https://github.com/isu-avista/data/releases/tag/v0.1.1) - 2020-11-13
### Added
- This document

### Changed
- README.md to be formatted according to GitHub guidelines

### Removed
- Nothing

## [0.1.0](https://github.com/isu-avista/data/releases/tag/v0.1.0) - 2020-11-13
### Added
- Setup the basic file structure
- Base classes forming the initial data model for the Avista Predictive Maintenance project.
- Added tests for each of the classes

### Changed
- Nothing

### Removed
- Nothing
