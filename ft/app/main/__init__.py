# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:24:30 2018

@author: hong
"""

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views
from . import errors