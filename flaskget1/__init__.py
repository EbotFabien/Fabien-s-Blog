from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager




app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='FABIENCLASSIC'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fabienflask.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'

from flaskget1 import routes