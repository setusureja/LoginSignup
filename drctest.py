#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
from prettytable import PrettyTable
from goto import with_goto
import hashlib
from email_validator import validate_email, EmailNotValidError

@with_goto
def Bar():
    mydb = mysql.connector.connect(user='setu', password='123',host='localhost',database='user')
    mycursor1 = mydb.cursor()
    label .start
    selection = int(input("Choose option\n 1.Login  2.Signup\n"))
    if(selection == 1):

        username = input("enter username")
        password = input("enter password")
        isSucess = False
        getAll = mycursor1.execute("SELECT id,email,username, password, created_at from user_info3")

        myresult1 = mycursor1.fetchall()
        password = hashlib.sha256(password.encode())
        password = password.hexdigest()
        #print(password)
        for x in myresult1:
            if(username == x[2] and password == x[3]):
                isSucess = True
                break;
        if(isSucess):
            print("Login Sucessful")
            t= PrettyTable(['id','email', 'username','created time'])
            for x in myresult1:
                t.add_row([x[0],x[1],x[2],x[4]])
            print(t)
        else:
            print("Entered a wrong password or username")
    if(selection == 2):
        label .signin
        email = input("Enter Email: ")
        username = input("enter username: ")
        password = input("enter password: ")
        cpassword = input("confirm password: ")
        created_at = datetime.now()
        try:
            valid = validate_email(email)
        except:
            print("invalid email")
            goto .signin
        if(password == cpassword):
            try:
                password = hashlib.sha256(password.encode())
                password = password.hexdigest()
                sql_command = "insert into user_info3(email,username, password, created_at) values('{0}','{1}','{2}','{3}')".format(email, username, password, created_at)
                mycursor1.execute(sql_command)
                mydb.commit()
                mycursor1.close()
                print("entry successfully inserted")
                goto .start
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
        else:
            print("Password mismatch")
            goto .start
Bar()

