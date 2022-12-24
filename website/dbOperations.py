import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        print(os.getcwd())
        dir = os.getcwd() + '\Webpage-main\website'
        conn = sqlite3.connect(os.path.join(dir,db_file))
    except Error as e:
        print(e)

    return conn


#when customer fills the form, add their data in the database for later analysis
def updateDB(phone,email,name):
    try:
        con = create_connection('customer.db')
        cur = con.cursor()
        cur.execute('insert into Customers (phone,email,name) values (?,?,?)',(phone,email,name))
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()


def checkEmails(email):
    try:
        con = create_connection('customer.db')
        cur = con.cursor()
        cur.execute('Select email from Customers')
        rows = cur.fetchall()
        emails = []
        for i in rows:
            #print(i[0])
            if i[0] == email:
                print(True)
                return True
        print(False)
        return False
        
    except Exception as e:
        print(e)
        con.rollback()

def checkUser(userid):
    try:
        con = create_connection('customer.db')
        cur = con.cursor()
        cur.execute('Select * from Admin')
        rows = cur.fetchall()
        users = []
        for i in rows:
            #print(i[0])
            if i[0] == userid:
                print('user : '+i[0]+' password : '+i[1])
                return i[1] #returning password 
        return False        
    except Exception as e:
        print(e)
        con.rollback()


if __name__ == '__main__':
    print('hello main : dbOperations.py')
    #checkEmails('manvi@gmail.com')
    checkUser('Ankit1234')

