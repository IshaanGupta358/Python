from RollNumber_Generate import *
import mysql.connector

db = mysql.connector.connect(host='localhost', password='2009', user='root')

def create():

    

    try:
        cursor = db.cursor()

        print("---------------------Wellcome-To-Create-User------------------------")



        roll_n = r_no
        f_name = str(input("Give the First Name: "))
        l_name = str(input("Give the Surname: "))
        clasS = int(input("Give its Grade: "))


        SQL = 'INSERT INTO `database_ishaan`.`students` (`R_no`, `F_Name`, `L_Name`, `Grade`) VALUES ("%s", "%s", "%s", "%s")'
        updateData = (roll_n,f_name,l_name,clasS)

        cursor.execute(SQL,updateData)

        db.commit()
        print("Succesful!!")

        roll = str(roll_n)

        print(f_name + " " + l_name + "'s Roll Number is: "+ roll )

        print("*"*50)

    except Exception as e:
        print(e)

        db.rollback()


