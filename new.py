from DataBase_Create import *
from DataBase_Update import *
from DataBase_Delete import *

print("\/"*15+"Wellcome-To-DataBase"+"\/"*15)

print("1: To Creat a User.")
print("2: To Update a User.")
print("3: To Delete a User.")
print("4: Quit")
print("Please enter the serial number to select the opption.")
usr = int(input("Your Response: "))

if usr ==1:
    create()
    print("\/"*40)
elif usr == 2:
    update()
    print("\/"*40)

elif usr == 3:
    delete()
    print("\/"*40)

else:
    print("\/"*40)    
    quit()
