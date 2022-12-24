import sqlite3
import os
from werkzeug.security import generate_password_hash,check_password_hash
def createTable():
    con = sqlite3.connect('G:\Kavita Lama Make up Artist\Webpage-main\website\customer.db')
    con.execute("create table Admin (userid TEXT PRIMARY KEY,password TEXT NOT NULL)");
    con.close()
    print("table created")

def showData():
    con = sqlite3.connect('G:\Kavita Lama Make up Artist\Webpage-main\website\customer.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Admin")
    rows = cur.fetchall()
    list = []
    for row in rows:
        list.append(row)
    print(list)
    if check_password_hash(list[1][1],'Kavita@12345'):
        print('password matched')
    else:
        print('password did not matched')

def insertData():
    con = sqlite3.connect('G:\Kavita Lama Make up Artist\Webpage-main\website\customer.db')
    cur = con.cursor()
    password = generate_password_hash('Kavita@12345', method='sha256')
    cur.execute('insert into Admin (userid,password) values (?,?)',('Kavita3256',password))
    con.commit()

def deleteData():
    con = sqlite3.connect('G:\Kavita Lama Make up Artist\Webpage-main\website\customer.db')
    cur = con.cursor()
    cur.execute('DELETE FROM Admin WHERE userid = \'Kavita3256\'')
    con.commit()

path = 'G:\Kavita Lama Make up Artist\Webpage-main\website\customer.db'
#createTable()
#insertData()
showData()
#deleteData()
#print(generate_password_hash("Ankit123456", method='sha256'))
#[('Ankit1234', 'ankit@12345'), ('Kavita3256', 'sha256$5CRdBdce4OgzpfEe$9ce9b9544773eb9fa47e5780141319efcf07680fa76c381a0dc2152f40c66fb1')]
