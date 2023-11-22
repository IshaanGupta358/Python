from tkinter import *
from RollNumber_Generate import *
import mysql.connector



db = mysql.connector.connect(host='localhost', password='2009', user='root')
   
def delete():
    try:
        cursor = db.cursor()

        root = Tk()
        

        def delete():
            row = option.get()
            SQL = 'UPDATE `database_ishaan`.`students` SET `Status` = "InActive" WHERE (`R_no` = %s)'
            updateData = [row]
            cursor.execute(SQL,updateData)
            db.commit()
            Label(root,text="Succesful!!").grid(row=7,column=3)

        def ok():

            global display1
            global display2
            global display3

            row = option.get()
            SQL = 'SELECT F_Name , L_Name , Grade FROM database_ishaan.students WHERE R_no = %s'
            updateData = [row]
            cursor.execute(SQL,updateData)
            
            rowD = cursor.fetchone()
            list3 = rowD

            

            obj1 = list3[0]
            obj2 = list3[1]
            obj3 = list3[2]

            
            display1 = Label(root, text= obj1, font="Play  10")
            
            display1.grid(row=3,column=3)

            display2 = Label(root, text = obj2)
            
            display2.grid(row=4,column=3)
            
            display3 = Label(root, text = obj3)
            
            display3.grid(row=5,column=3)

        def refresh():

            display1.delete(0,END)
            display2.delete(0,END)
            display3.delete(0,END)
            

        cursor.execute("SELECT R_no FROM database_ishaan.students Where Status = 'Active'")
        result = cursor.fetchall()
        
        r = str(result)
        s = ''.join(x for x in r if x.isdigit())
         
        row_count = list(s)
        
        




        option = StringVar(root)
        op = OptionMenu(root,option, *row_count).grid(row=2,column=3)


        Button(root,text="Delete",command=delete).grid(row=6,column=3)

        
        Label(root,text="Select Roll Number:").grid(row=2,column=2)

        root.title("Delete Window")
        root.geometry("260x200")
        Label(root, text="Delete User", font="Arial 15 bold").grid(row=0,column=3)
            
        
        Label(root, text="First Name:").grid(row=3,column=2)
        Label(root, text="Last Name").grid(row=4,column=2)
        Label(root, text="Grade:").grid(row=5,column=2)

        


        roll_n = r_no
        f_name = StringVar()
        l_name = StringVar()
        clasS = StringVar()

        
        Button(root,text="OK",command=ok).grid(row=2,column=4)
        Button(root,text="Quit",command=root.destroy).grid(row=8,column=3)
        Label(root,text=" ").grid(row=7,column=2)

    
        root.mainloop()

    except Exception as e:
        print(e)

        db.rollback()
