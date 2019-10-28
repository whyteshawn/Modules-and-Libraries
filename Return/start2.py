#-----------------------------
#start2.py
#Shawn Whyte
#The main file of a program
#path - \\return
#-----------------------------

import number #looks into the same folder folder and imports the program number.py

print("I'm looking in the main folder and importing the file number.py")

returned_value = number.first(4) #accesses the number.py file and pass the value 4 into the function FIRST.
#Save that returned value

print(returned_value) #print the number stored in the variable 

print("I am running", number.file_name) #you can also access a variable directly