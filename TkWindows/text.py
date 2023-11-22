# import re
 
# # initializing number
# test_num = "12345678910"
 
# # printing original number
# print("The original number is : " + str(test_num))
 
# # Using re.sub()
# # Adding comma between numbers

# res = re.sub(r'(\d{2})(?=\d)', r'\1,', str(test_num)[::9])[0::]
 
# # printing result
# print("The number after inserting commas : " + str(res))
# #This code is contributed by Edula Vinay Kumar Reddy

an_int = 1357910

list_of_digits = [int(x) for x in str(an_int)]

print(list_of_digits)  #  [1, 3, 5, 7, 9]

