"""The ISU Avista Data Module which contains the basic classes used to interface between the system and the database.
"""
from avista_data import config_item
from avista_data import data_point
from avista_data import device
from avista_data import issue
from avista_data import security_config
from avista_data import server_config
from avista_data import sensor
from avista_data import user
from avista_data import server
from avista_data import status
from avista_data import api_key
from avista_data import role_too_low_error
from avista_data import database


# def add_user(json):
#     return User(json)
#
#
# def delete_user(email):
#     usr = find_user(email)
#     if usr:
#         db.session.remove(user)
#         db.session.commit()
#
#
# def update_user(email, json):
#     usr = find_user(email)
#     if usr:
#         usr.update(json)
#
#
# def find_user(email):
#     return User.query.filter_by(email=email).first()
#
#
# def add_device(json):
#     return device.Device(json)
#
#
# def delete_device(name):
#     dvc = find_device(name)
#     if dvc:
#         db.session.remove(dvc)
#         db.session.commit()
#
#
# def update_device(name, json):
#     dvc = find_device(name)
#     dvc.update(json)
#
#
# def find_device(name):
#     return device.Device.query.filter_by(name=name).first()
#
#
# def add_data_point():
#     pass
#
#
# def delete_data_point():
#     pass
#
#
# def update_data_point():
#     pass
#
#
# def find_data_point():
#     pass
#
#
# def add_config_item():
#     pass
#
#
# def delete_config_item():
#     pass
#
#
# def update_config_item():
#     pass
#
#
# def find_config_item():
#     pass
#
#
# def add_issue():
#     pass
#
#
# def delete_issue():
#     pass
#
#
# def update_issue():
#     pass
#
#
# def find_issue():
#     pass
#
#
# def add_status():
#     pass
#
#
# def delete_status():
#     pass
#
#
# def update_status():
#     pass
#
#
# def find_status():
#     pass
#
#
# def add_sensor():
#     pass
#
#
# def delete_sensor():
#     pass
#
#
# def update_sensor():
#     pass
#
#
# def find_sensor():
#     pass
#
#
# def add_server():
#     pass
#
#
# def delete_server():
#     pass
#
#
# def update_server():
#     pass
#
#
# def find_server():
#     pass
#
#
# def add_sensor_parameter():
#     pass
#
#
# def delete_sensor_parameter():
#     pass
#
#
# def update_sensor_parameter():
#     pass
#
#
# def find_sensor_parameter():
#     pass
#
#
# def add_security_config():
#     pass
#
#
# def delete_security_config():
#     pass
#
#
# def update_security_config():
#     pass
#
#
# def find_security_config():
#     pass
