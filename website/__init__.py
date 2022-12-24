from flask import *
from flask_mail import *  
from flask_restful import Resource, Api
import os
import sqlite3

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
    mail = Mail(app)
    app.config['MAIL_OBJECT'] = mail
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app



