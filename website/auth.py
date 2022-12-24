from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
from .dbOperations import *
auth = Blueprint('auth',__name__)
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userId = request.form.get('userid')
        password = request.form.get('password')
        print('user id : '+userId+' , password : '+password)
        existUser = checkUser(userId)
        if not existUser:
            print('user doesnot exist')
            flash('User doesnot exist',category='error')
        else:
            dbPass = existUser
            if check_password_hash(dbPass,password):
                print('correct password')
                #print()
                return redirect(url_for('auth.adminGallery'))
            else:
                flash('Wrong password',category='error')
            #print('user exists : '+dbPass)
    return render_template('login.html',user='')

@auth.route('/adminGallery',methods=['GET'])
def adminGallery():
    return render_template('adminGallery.html',user='')