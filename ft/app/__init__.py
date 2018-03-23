# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 22:25:15 2018

@author: hong
"""

#import sys
#sys.path.append('C:\\Users\\hong\\Desktop\\ft')

from flask import Flask,render_template,flash,redirect,session,url_for,request
import time
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    #sys.path.append('C:\\Users\\hong\\Desktop\\ft\\app\\main')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
    

'''
app = Flask(__name__)
#app.config.from_object('config')
app.config['SECRET_KEY'] = 'hard to guess string'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/world?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

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

class NameForm(FlaskForm):
    name = StringField("what is your name?",validators=[Required()])
    submit = SubmitField("Sumbit")

@app.route("/abc")
def index():
    return render_template('header.html')

@app.route("/xxx")
def hi():
    return render_template('new.html',name=session.get("name"))

@app.route("/test",methods=["Get","POST"])
def cao():
    form = NameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.name.data).first()
            if user is None:
                user = User(username = form.name.data)
                db.session.add(user)
                session['known'] = False
            else:
                session['known'] = True
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('hi'))
        
            
            #old_name = session.get('name')
            #if old_name is not None and old_name != form.name.data:
                #flash("look like you have changed your name")
        
            #session['name'] = form.name.data
            #time.sleep(2)      
            #return redirect(url_for('hi'))
            
    
        
        #session['name'] = form.name.data
        #return redirect(url_for('hi'))
    
    
    return render_template("cao.html",form=form)
if __name__ == '__main__':
    app.run(debug=True)
    
'''
    