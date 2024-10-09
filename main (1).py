# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:08:41 2024

@author: gcook
"""
# Import the two modules that hold the classes and utilities
import inv_utilities as u
from inv_classes import Equipment, Computer, User


"""
 Create a menu to process the files
   ------------------------------------
     Process User and Equipment Files
   ------------------------------------
       A - Process User and csv files
       B - Process Equipment csv file
       C - Print User Listing
       D - Print Equipment Listing
       E - Exit
      
 Note: Only show C and/or D if the file(s) have already been loaded
 
 The prompt for the user should ask for the selection (allow the user to input
    either uppercase or lowercase letters)
"""
def get_yes_or_no (prompt):
    done = False
    prmpt = prompt + ": "
    while not done:
        yes_or_no = input(prmpt)
        if yes_or_no.upper() == "Y" or yes_or_no.upper() == "N":
            done = True
    
    return(yes_or_no.upper())

    
new_user_file = list()
new_equipment_file = list()

done = False
while not done:
    opt_list = "(A,B,"
    print ("-"*36)
    print("  Process User and Equipment Files")
    print ("-"*36)
    print ("   A - Process User csv file\n",
           "  B - Process Equipment csv file")
    try:
        if len(new_user_file) > 0:
            print ("   C - Print User Listing")
            opt_list += "C,"
    except TypeError:
        pass
    try:
        if len(new_equipment_file) > 0:
            print ("   D - Print Equipment Listing")
            opt_list += "D,"
    except TypeError:
        pass
    print ("   E - Exit\n\n")
    
    opt_list += "or E)"
    
    choice = input(f"What would you like to do {opt_list}: ")
    try:
        if choice.upper() == "A":
            fname = input ("Enter the User csv filename: ")
            new_user_file = u.load_user_file(fname)
        elif choice.upper() == "B":
            fname = input ("Enter the Equipment csv filename: ")
            new_equipment_file = u.load_equipment_file(fname)

        elif choice.upper() == "C":
            if get_yes_or_no("Show only active?") == "Y":
                u.print_user_listing(new_user_file, True)
            else:
                u.print_user_listing(new_user_file, False)
        elif choice.upper() == "D":
            if get_yes_or_no("Show only active?") == "Y":
                u.print_equipment_listing(new_equipment_file, True)
            else:
                u.print_equipment_listing(new_equipment_file)
        elif choice.upper() == "E":
            done = True
        else:
            print ("\n  Please enter A, B, or E\n")
    except FileNotFoundError:
        print("File not found")
        
        


