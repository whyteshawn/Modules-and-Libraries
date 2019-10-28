#-----------------------------
#start1.py
#Shawn Whyte
#The main file of a program
#path - \\main1
#-----------------------------

import hi #looks into the same folder folder and imports the program hi.py

print("I'm looking in the main folder and importing the file hi.py")

hi.greeting("Student") #accesses the hi.py file and passes the string STUDENT into the function GREETING for printing

print("I am running", hi.file_name) #you can also access a variable directly

print(hi.new_list[2]) #accessing a list value in hi.py with index number 2

print(hi.new_dictionary["b"]) #accessing a dictionary value with key "b" in hi.py