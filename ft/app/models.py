# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:30:07 2018

@author: hong
"""
from app import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref = 'role')
    
    def __repr__(self):
        return ' <Role %r> '%self.name
        
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return ' <User %r> '%self.username