from tkinter import *
from RollNumber_Generate import *
import mysql.connector

db = mysql.connector.connect(host='localhost', password='2009', user='root')



def create():    

    try:
        cursor = db.cursor()

        def c():



            r = roll_n
            f = f_name.get()
            l = l_name.get()
            c = clasS.get()
            SQL = "INSERT INTO `database_ishaan`.`students` (`R_no`, `F_Name`, `L_Name`, `Grade`, `Status`) VALUES (%s, %s, %s, %s, 'Active');"

            
            updateData = (r,f,l,c)

            
            cursor.execute(SQL,updateData)

            Label(root,text="Succesful!!").grid(row=6,column=3)
            Label(root,text= text2).grid(row=7,column=3)

            

            db.commit()


       
            

        


        root = Tk()
        
        

        

        root.title("Create Window")
        root.geometry("260x200")
        Label(root, text="Create User", font="Arial 15 bold").grid(row=0,column=3)
            
        
        Label(root, text="First Name:").grid(row=3,column=2)
        Label(root, text="Last Name").grid(row=4,column=2)
        Label(root, text="Class:").grid(row=5,column=2)

        grade = ["1",'2',"3",'4',"5",'6',"7",'8',"9",'10',"11",'12']


        roll_n = r_no
        f_name = StringVar(root)
        l_name = StringVar(root)
        clasS = StringVar(root)

        Entry(root,textvariable=f_name).grid(row=3,column=3)
        Entry(root,textvariable=l_name).grid(row=4,column=3)
        OptionMenu(root,clasS, *grade).grid(row=5,column=3)

        Button(root,text="Save",command=c).grid(row=6,column=3)
        Button(root,text="Quit",command=root.destroy).grid(row=8,column=3)
        Label(root,text=" ").grid(row=7,column=2)

        list3 = str(r_no)

        text2 = "User's Roll Number is: " + list3

        
    
        root.mainloop()

    except Exception as e:
        print(e)

        db.rollback()

