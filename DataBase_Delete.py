
import mysql.connector

db = mysql.connector.connect(host='localhost', password='2009', user='root')

def delete():

    try:
        cursor = db.cursor()

        print("---------------------Wellcome-To-Delete-User------------------------")


        table = "students"
        r_no = int(input("Give User's Roll Number: "))
        

        SQL = "DELETE FROM database_ishaan.students WHERE R_no = %s"
        updateData = [r_no]

        cursor.execute(SQL,updateData)

        db.commit()
        print("Succesful!!")

        print("*"*50)

    except Exception as e:
        print(e)

        db.rollback()



