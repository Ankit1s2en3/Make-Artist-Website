from flask import *
from flask_mail import *  
import json, os
import sqlite3
from flask_restful import Resource, Api
import re
from .dbOperations import *
views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])

def home():
    return render_template('index.html')


#gallery page
@views.route('/gallery')

def gallery():
    imgFiles = os.listdir(current_app.config['UPLOAD_FOLDER'])
    print(imgFiles)
    return render_template('gallery.html',images = imgFiles)

#gallery test
@views.route('/galleryTest')
def gallerTest():
    imgFiles = os.listdir(current_app.config['UPLOAD_FOLDER'])
    print(imgFiles)
    return render_template('galleryTest.html',images = imgFiles)

#get mails when customer fills the form
@views.route('/mail_customer_data',methods=['POST'])

def mail_customer_data():
    if request.method == 'POST':
        mail = current_app.config['MAIL_OBJECT']
        name = request.form['name']
        email = request.form['email']
        phone =  request.form['phone']
        message = request.form['message']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(name) < 3 :
            flash('Name must be greater than 2 characters.',category='error')
        elif re.fullmatch(regex, email):
            flash('Please enter correct email.',category='error')
        elif len(phone) < 10:
            flash('Please enter correct number.',category='error')
        else:
            body = 'name : '+name+' \nemail : '+email+' \nphone : ' +phone+' \nmessage : ' + message
            msg = Message('your customer details',sender='ankit414sen280@gmail.com', recipients=['ankitsen.charmingone1@gmail.com'])
            msg.body = body
            if not checkEmails(email):
                #adding new email if it doesnot exists
                print('updating the email')
                updateDB(phone,email,name)
            flash('We have received your mail. We will get in touch!',category='success')
            #mail.send(msg)

        return redirect(url_for('views.home')+'#contact')


#ned to work on post method on this
@views.route('/sendOffers',methods=['GET'])
def sendOffers():
    list = []
    try:
        conn = sqlite3.connect('customer.db')
        cur = conn.cursor()
        cur.execute("SELECT email FROM Customers")
        rows = cur.fetchall()
        for row in rows:
            list.append(row[0])

        return jsonify({'data':list})

        msg = Message('your customer details',sender='ankit414sen280@gmail.com', recipients=list)
        msg.body = message
        mail.send(msg)
    except Exception as e:
        print(e)
        return 'Unable to process the response'




#showing the upload page
@views.route('/upload-page')
def upload_Page():
    return render_template('upload.html')

#photo upload
@views.route('/photoUpload',methods=['POST'])
def uploading():
    print('request method : '+request.method)
    if request.method == 'POST':
        print(request.files.keys())
        f = request.files['photo']
        print("uploaded file name : "+f.filename)
        img_loc = current_app.config['UPLOAD_FOLDER']
        f.save(os.path.join(img_loc,f.filename))
        return "Successful"

@views.route('/base')
def base():
    return render_template('base.html')

@views.route('/page')
def page():
    return render_template('page.html')