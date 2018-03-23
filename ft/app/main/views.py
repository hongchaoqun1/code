# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:26:29 2018

@author: hong
"""

from datetime import datetime
from flask import render_template,session,redirect,url_for

from . import main
#from .forms import NameForm
#from .. import db
#from  ..models import User

@main.route('/abc',methods=['GET','POST'])
def index():
    return render_template('header.html')