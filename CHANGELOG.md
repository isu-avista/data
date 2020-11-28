# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
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

## [0.1.3] - 2020-11-25
### Added
- New migration for datapoint

### Changed
- Added a new field to Datapoint to incorporate the timestamp of the data

### Removed
- Nothing

## [0.1.2] - 2020-11-13
### Added
- Nothing

### Changed
- Updated setup.py to accurately reflect the module name and version

### Removed
- Nothing

## [0.1.1] - 2020-11-13
### Added
- This document

### Changed
- README.md to be formatted according to GitHub guidelines

### Removed
- Nothing

## [0.1.0] - 2020-11-13
### Added
- Setup the basic file structure
- Base classes forming the initial data model for the Avista Predictive Maintenance project.
- Added tests for each of the classes

### Changed
- Nothing

### Removed
- Nothing
