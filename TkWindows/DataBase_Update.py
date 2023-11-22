import itertools
from tkinter import *
import mysql.connector


db = mysql.connector.connect(host='localhost', password='2009', user='root')

def update():

    try:
        cursor = db.cursor()

        

        def getV():

            global display1
            global display2
            global display3
            global obj1
            global obj2
            global obj3
            
            
            row = option.get()
            SQL = 'SELECT F_Name , L_Name , Grade , Status = "Active" FROM database_ishaan.students WHERE R_no = %s'
            updateData = [row]
            cursor.execute(SQL,updateData)
            rowD = cursor.fetchone()
            list3 = rowD

            


            obj1 = list3[0]
            obj2 = list3[1]
            obj3 = list3[2]

                    

            
            display1 = Entry(root, textvariable=Fnameval)
            display1.insert(0,obj1)
            display1.grid(row=3,column=3)

            display2 = Entry(root, textvariable=Lnameval)
            display2.insert(0,obj2)
            display2.grid(row=4,column=3)
            
            display3 = Entry(root, textvariable=classval)
            display3.insert(0,obj3)
            display3.grid(row=5,column=3)     


        def refresh():

            display1.delete(0,END)
            display2.delete(0,END)
            display3.delete(0,END)


        def GUpdate():



            r = option.get()
            f = Fnameval.get()
            l = Lnameval.get()
            c = int(classval.get())

            if c > 12:
                Label(root,text="Invalid Input!!").grid(row=9,column=3)
                Label(root,text=" Check The Ditails Again").grid(row=10,column=3)
                Label(root,text="ERROR!!").grid(row=7,column=3)


            if c < 13:

                SQL = 'UPDATE `database_ishaan`.`students` SET `F_Name` = %s, `L_Name` = %s, `Grade` = %s WHERE (`R_no` = %s)'
                
                updateData = (f,l,c,r)

                
                cursor.execute(SQL,updateData)

                Label(root,text="Succesful!!").grid(row=7,column=3)


                db.commit()
                root.update()
                root.update_idletasks()

        
        cursor.execute("SELECT R_no FROM database_ishaan.students Where Status = 'Active'")
        result = cursor.fetchall()
        
        r = str(result)
        s = ''.join(x for x in r if x.isdigit())   

         
        row_count = list(str(s))

        print(row_count)

        

        
       
        root = Tk()


        root.title("Update Window")
        root.geometry("320x240")
        Label(root, text="Update User", font="Arial 15 bold").grid(row=0,column=3)

        Label(root, text="Roll No.").grid(row=2,column=2)
        Label(root, text="First Name").grid(row=3,column=2)
        Label(root, text="Last Name").grid(row=4,column=2)
        Label(root, text="Class").grid(row=5,column=2)

        rollval = IntVar()
        Fnameval = StringVar(root)
        Lnameval = StringVar(root)
        classval = StringVar(root)


        option = StringVar(root)
        OptionMenu(root,option, *r).grid(row=2,column=3)

        row = option.get()

        def refreshw():
            root.update()
            root.update_idletasks()
        

        root.counter = 0

        def clicked():
            root.counter = root.counter + 1

            

            if root.counter <= 2:
                Button(root,text="Ok",command=lambda:[getV(),clicked2()]).grid(row=2,column=4)

            if root.counter > 2 :

                refresh()
                Button(root,text="Ok",command=getV()).grid(row=2,column=4)
                root.counter = root.counter - 1
                

        def clicked2():
            root.counter = root.counter + 1

            if root.counter <= 2:
                Button(root,text="Ok",command=lambda:[getV(),clicked()]).grid(row=2,column=4)

            
            n=10^1000000000000000000            

            if root.counter in range(2,n):
                refresh()
                Button(root,text="Ok",command=getV()).grid(row=2,column=4)
                root.counter = root.counter - 2

                clicked()
                    
     

        Button(root,text="Ok",command=clicked2).grid(row=2,column=4)
        
        Button(root,text="Save",command=lambda:[GUpdate(),refresh()]).grid(row=6,column=3)
        
        

        Button(root,text="Quit",command=root.destroy).grid(row=8,column=3)
        Label(root,text=" ").grid(row=7,column=2)

        root.mainloop()



        
    except Exception as e:
        print(e)

        db.rollback()

update()