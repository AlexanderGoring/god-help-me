import csv
from inv_classes import User, Equipment, Computer

def load_user_file(infile):
    """
    The load_user_file() function will process a .csv file and return a 
    list of class User
    
    Parameters:
    ------------
        infile:
            the name of the csv file to be processed
        
    An example csv file shows the structure of the csv:
        UserID,FirstName,LastName,Status
        E1221377,Gregory,Cook,active
        S1113954,Emelia,Hayes,active
        S1137091,Louis,Mejia,active
        
    Returns
    -------
        a list of tuples containing the data from class User
    """
    try:
        #create an empty list to hold each row in the file
        proc_list = []

        with open(infile, 'r') as f:
            # create a csv.reader()
            user_reader = csv.reader(f)

            # keep track of the number of lines read
            line_count = 0
            for row in user_reader:
                # loop through the file.  Do not process the header row
                if line_count > 0:
                    # create a new User instance using the data from the file
                    new_user = User(row[0], row[2], row[1])
                    new_user.status = row[3]

                    # add the new user instance to the list
                    proc_list.append(new_user)
                line_count += 1

        # return the populated list of User instances      
        return proc_list
    except IndexError:
            print("File is invalid")

def load_equipment_file(infile):
    """
    Parameters
    ----------
    infile :
        A .csv file containing equipment information
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    a list of tuples containing the data from classes Equipment and sub-classes

    """
    
    try:
        #create an empty list to hold each row in the file
        equip_list = []

        with open(infile, 'r') as f:
            # create a csv.reader()
            e_reader = csv.reader(f)

            # keep track of the number of lines read        
            line_count = 0
            for row in e_reader:
                # loop through the file.  Do not process the header row
                if line_count > 0:
                    print (len(row))
                    # determine the category of the piece of equipment from the row
                    cat = row[1]

                    # depending on the category, you will create an instance of type Computer or type Equipment
                    if cat == 'PC' or cat == 'Server':
                        # create a new Computer instance using the data from the file
                        comp = Computer(row[0], row[1], row[2], row[4])
                        comp.os = row[3]
                        comp.status = row[6]
                        # add the new Computer instance to the list
                        equip_list.append(comp)
                    else:
                        # create a new Computer instance using the data from the file
                        eq = Computer(row[0], row[1], row[2], row[4])
                        eq.status = row[6]
                        # add the new Equipment instance to the list
                        equip_list.append(eq)
                line_count += 1

        return(equip_list)
    except IndexError:
        print("File is invalid")

def print_user_listing(user_list, show_active_only = False):
    """
    The print_uers_listing() displays formatted list of users to the screen
    
    Parameters
    ----------
    user_list:
        a list of tuples containing the: (username, lastname, firstname, status)
    show_active_only:
        if this is set to True, then only those user records with a status of 'active' is displayed
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    print_user_function returns Nothing.  
    """
    
    # print a header row:
        
    # loop throught the list and display the information in each tuple in the list. 
    # if the show_active_only attribute is True, only display the user information that has a status of 'active'
    print("-"*45)
    print(" User Listing")
    print("-"*45)
    print("Username Name (Last, First)          Status")
    print("-"*45)
    if show_active_only == True:
        for row in user_list:
            if row.get_status() == "active":
                print(row.get_username(), row.get_lastname(),row.get_firstname(),row.get_status())
    else:
        for row in user_list:
            print(row.get_username(), row.get_lastname(),row.get_firstname(),row.get_status())

def print_equipment_listing(equipment_list, show_active_only = False):
    """
    The print_equipment_listing() displays formatted list of computers and other quipment to the screen
    
    Parameters
    ----------
    equipment_list:
        a list of tuples containing the: (uuid, category, device, os, location, value, status) if it represents 
          a computer or (uuid, category, device, location, value, status) if it represents other equipment
        
    show_active_only:
        if this is set to True, then only those user records with a status of 'active' is displayed
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    print_equipment_listing_function returns Nothing.  
    """
    
    # print a header row:
        
    # first loop through the list and display the information about computers in the tuples in the list. 
    # Then loop through the list and display the information about other equipment in the tuples in the list
    # if the show_active_only attribute is True, only display the user information that has a status of 'active'
    print("="*45)
    print(" Equipment Listing")
    print("="*45)
    print("-"*45)
    print("Computers")
    print("-"*45)
    print("UUID Category    Device   OS   Status")
    print("-"*45)
    if show_active_only == True:
        for row in equipment_list:
            if row.get_status() == "active":
                if row[1] == "Computer" or "Server":
                    print(row.get_uuid(), row.get_category(),row.get_device(), row.get_OS(), row.get_status())
        print("="*45)
        print("  Other Equipment")
        print("="*45)
        print("UUID Category Device OS Status")
        for row in equipment_list:
            if row.get_status() == "active":
                if row[1] != "Computer" or "Server":
                    print(row.uuid(), row.category(), row.device(), row.status())
    else:
        for row in equipment_list:
            if row.get_category() == "PC" or row.get_category() == "Server":
                print(row.get_uuid(), row.get_category(),row.get_device(), row.get_os(), row.get_status())
        print("="*45)
        print("  Other Equipment")
        print("="*45)
        print("UUID Category Device OS Status")
        for row in equipment_list:
            if row.get_category() == "Switch":
                print(row.get_uuid(), row.get_category(), row.get_device(), row.get_status())

                              
                
