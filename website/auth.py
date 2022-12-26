from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
from .dbOperations import *
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Customer
from . import db
auth = Blueprint('auth',__name__)
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userId = request.form.get('userid')
        password = request.form.get('password')
        print('user id : '+userId+' , password : '+password)
        user = User.query.filter_by(userId=userId)
        user = user.first()
        if user:
            if check_password_hash(user.password,password):
                print('correct password')
                return redirect(url_for('auth.adminGallery'))
            else:
                flash('Wrong password',category='error')
        else:
            print('user doesnot exist')
            flash('User doesnot exist',category='error')

    return render_template('login.html',user='')

@auth.route('/adminGallery',methods=['GET'])
def adminGallery():
    return render_template('adminGallery.html',user='')

'''''
@auth.route('/signup',methods=['GET','POST'])
def signup():
    new_user = User(name="Kavita",userId="kavita341",password=generate_password_hash("Kavita@3256", method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return 'done'
'''

@auth.route('/checkdb',methods=['GET','POST'])
def check():
    users = db.session.execute(db.select(Customer)).scalars().all()
    print('-----')
    print(users)
    return 'done'
