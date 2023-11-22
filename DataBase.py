from DataBase_Create import *
from DataBase_Update import *
from DataBase_Delete import *

print("Wellcome-To-DataBase")

print("1: To Creat a User.")
print("2: To Update a User.")
print("3: To Delete a User.")
print("4: Quit")
print("Please enter the serial number to select the opption.")
usr = int(input("Your Response: "))

if usr ==1:
    create()
    
elif usr == 2:
    update()
   
elif usr == 3:
    delete()
    

else:
   
    quit()
