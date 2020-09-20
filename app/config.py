from os import environ


class Config(object):
    SECRET_KEY = environ.get('SDPF_FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SDPF_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
