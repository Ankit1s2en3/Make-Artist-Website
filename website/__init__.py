from flask import *
from flask_mail import *  
from flask_restful import Resource, Api
import os
import sqlite3
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy #

db = SQLAlchemy() #
DB_name = "database.db" #

def createApp():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'Webpage-main\website\static\images'
    app.config['SECRET_KEY'] = 'kjhasdfhasjdkljsa'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'ankit414sen280@gmail.com'
    app.config['MAIL_PASSWORD'] = 'atpcqdlyyqyudaby'
    app.config['MAIL_USE_TSL'] = False
    app.config['MAIL_USE_SSL'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_name}' #
    
    mail = Mail(app)
    app.config['MAIL_OBJECT'] = mail

    db.init_app(app) #
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import Customer,User#

    with app.app_context(): #
        db.create_all()

    login_manager = LoginManager()#
    login_manager.login_view = 'auth.login'#
    login_manager.init_app(app)#

    @login_manager.user_loader#
    def load_user(id):#
        return User.query.get(int(id))#

    return app

