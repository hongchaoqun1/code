# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Thu Mar 22 14:12:03 2018

@author: hong
"""

import os
from app import create_app,db
from app.models import User,Role
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app = app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()