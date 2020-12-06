# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

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
