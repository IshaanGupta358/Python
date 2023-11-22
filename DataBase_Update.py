from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', password='2009', user='root')

true = True

def update():
    while True:

        try:
            cursor = db.cursor()

            print("---------------------Wellcome--To--Updater------------------------")
            print("1: To Update Roll Number.")
            print("2: To Update Frist Name.")
            print("3: To Update Last Name.")
            print("4: To Update Class.")
            print("5: Quit")
            print("Please enter the serial number to select the opption.")

            usr = int(input("Your Response: "))

            if usr == 1:

                r_no = int(input("Enter the Roll Number of the student: "))
                UR_no = int(input("Enter the change roll number: "))

                SQL = 'update database_ishaan.students set R_no = %s where R_No = %s'
                updateData = (UR_no,r_no)

                cursor.execute(SQL,updateData)

                db.commit()
                print("Succesful!!")

                # user = str(input("Do you want to quit(Y/n)?"))

                # if user == "Y" or "y" :
                    
                    

                print("*"*50)

                true = False

            elif usr == 2:

                r_no = int(input("Enter the Roll Number of the student: "))
                fname = str(input("Enter the change First: "))

                SQL = 'update database_ishaan.students set F_Name = %s where R_No = %s'
                updateData = (fname,r_no)

                cursor.execute(SQL,updateData)

                db.commit()

                print("Succesful!!")
                print("*"*50)

                true = False

            elif usr == 2:

                r_no = int(input("Enter the Roll Number of the student: "))
                lname = str(input("Enter the change Last Name: "))

                SQL = 'update database_ishaan.students set L_Name = %s where R_No = %s'
                updateData = (lname,r_no)

                cursor.execute(SQL,updateData)

                db.commit()

                print("Succesful!!")
                print("*"*50)

                true = False


            elif usr == 4:

                r_no = int(input("Enter the Roll Number of the student: "))
                cla = int(input("Enter the change Class: "))


                SQL = 'update database_ishaan.students set Class = %s where R_No = %s'
                updateData = (cla,r_no)

                cursor.execute(SQL,updateData)

                db.commit()

                print("Succesful!!")
                print("*"*50)

                true = False


            elif usr == 5:

                true = False

            else:
                print("Invalid input")
                print("*"*50)

                true = False

        except Exception as e:
            print(e)

            db.rollback()

            true = False



