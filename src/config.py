#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Flask config."""

#import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))
database_file = "sqlite:///{}".format(path.join(basedir, "bookdatabase.db"))


class DevConfig:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True
    #SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = database_file#environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
