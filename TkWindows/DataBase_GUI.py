from DataBase_Create import *
from DataBase_Update import *
from DataBase_Delete import *
from tkinter import *

root = Tk()
img = PhotoImage(file='logo.png')
root.iconphoto(False, img)
Label(root,text="Wellcome To Student Database",font="Arial 20 bold").grid(row=2,column=3)
root.title("Wellcome Window")
root.geometry("1100x500")
Label(root, text="  ").grid(row=3,column=3)
Button(root,text="Create User",command=create).grid(row=4,column=3)
Label(root, text="  ").grid(row=5,column=3)
Button(root,text="Update User",command=update).grid(row=6,column=3)
Label(root, text="  ").grid(row=7,column=3)
Button(root,text="Delete User",command=delete).grid(row=8,column=3)

Label(root,text="Developed By Ishaan").grid( row= 10 , column=2)

photo = PhotoImage(file = "BASE.png")

Label(root,i=photo).grid(row=1,column=3)



root.mainloop()