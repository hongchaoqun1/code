# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:39:01 2018

@author: hong
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN =True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/world?charset=utf8'
    
class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass
    
config = {
        'development':DevelopmentConfig,
        'default':DevelopmentConfig
        }