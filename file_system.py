"""
File: file_system.py
Author: Muhammad Umar
Date: 12/9/22
Lab Section: 43
Email:  mumar2@umbc.edu
Description:  GL-System. Uses commands like rm, cd, ls, touch, locate and many others.
"""
root_system = {"file": [], "directory": {}}
PWD = "pwd"
LS = "ls"
TOUCH = "touch"
CD = "cd"
RM = "rm"
RMDIR = "rmdir"
LOCATE = "locate"
MKDIR = "mkdir"
EXIT = "exit"
SINGLE = 1
DOUBLE = 2
ZERO = 0
SINGLE_DOT = "."
DOUBLE_DOT = ".."
SLASH = "/"
EMPTY_STRING = ""
SPACED_STRING = " "

current_dir = root_system
file_list = []
temp = ""
user_input = ""
temp_dir = {}
old_dir = {}
temp_string = ''
filename = ""
old_dir = root_system
temp_history = []
flag = True
location_history = []
count = 0


def mkdir(new_dir, current_dir):
    """
      This function makes a directory inside a directory
      :param new_dir: A string that holds the name of the new directory
      :param current_dir: It is a dictionary which stores the current directory that the system is on.
      :return: None
      """
    if new_dir not in current_dir["directory"]:
        # Checks if the new directory key is not inside the current directory
        current_dir["directory"][new_dir] = {"file": [], "directory": {}}
        # If not, then it creates a new directory inside the current directory
    else:
        print("Directory already exists")
        # Informs the user that the same named directory is already inside the current directory


def cd_current(new_dir, current_dir):
    """
      This function changes a directory when a directory name is added next to the command cd.
      :param new_dir: A string that holds the name of the new directory
      :param current_dir: It is a dictionary which stores the current directory that the system is on.
      :return current_dir:It is a dictionary which stores the current directory that the system is on.
      :return new_dir: It is a dictionary which stores the new directory that the system is on.
      """
    temp_dir = {}
    location = {}
    location = access_directory(current_dir)
    # Accesses the current directory.
    if new_dir in location:
        # Check if the new directory is inside the current directory
        temp_dir = location[new_dir]
        # Changes to the new directory
        return temp_dir
    else:
        # Informs the user that the directory does not exist.
        print("Error, directory does not exist")
        # Directory does not change
        return current_dir


def access_directory(current_dir):
    """
      This function accesses the directory with the key word "directory".
      :param current_dir: It is a dictionary which stores the current directory that the system is on.
      :return location: It is a dictionary which stores the new directory that the system is on.
      """
    pos = {}
    location = {}
    pos = current_dir
    location = pos["directory"]
    # Access the directory
    return location


def access_file(current_dir):
    """
       This function accesses the file list with the key word "file".
       :param current_dir: It is a dictionary which stores the current directory that the system is on.
       :return location: It is a list which stores the current file list in the directory
       """
    pos = {}
    location = []
    pos = current_dir
    location = pos["file"]
    # Accessing the file list
    return location


def ls_current(current_dir, history, root_system):
    """
       This function prints the contents in the directory.
       :param current_dir: It is a dictionary which stores the current directory that the system is on.
       :param history: A list that holds the complete path to the directory.
       :param root_system: A dictionary that holds all the directories and files.
       :return: None
       """
    location = {}
    file = []
    keys = ""
    filename = ""

    location = access_directory(current_dir)
    # Accesses the directory
    file = access_file(current_dir)
    # Accesses the file
    if current_dir == root_system:
        print(f"Contents for /")
        print("         ..")
        # Checks if current_dir is equal to the root_system.
        # Special case needs a different print statement.
    else:
        print(f"Contents for {pwd(history)}")
        print("         ..")
    for keys in location:
        print(f"         {keys}")
    for filename in file:
        print(f"         {filename}")


def touch(filename, current_dir, root_system):
    """
    This function adds a new file into the file list.
       :param current_dir: It is a dictionary which stores the current directory that the system is on.
       :param filename: It is a string which holds the file name.
       :param root_system: A dictionary that holds all the directories and files.
       """
    pos = []
    temp_list = []
    old_pos = {}
    if len(filename) == 2 and filename[0] == "/":
        # Checks if only data is entered in this format '/filename'
        pos = access_file(current_dir)
        # Accesses file list in directory
        pos.append(filename[1:])
        # Appends file name inside the list
        file_list.append(filename[1:])
        # Adds file name to a file history list
    else:
        if filename[0] == "/":
            # Checks if the whole address is given
            old_pos = current_dir
            if filename[len(filename) - 1] == "/":
                # Checks if the last character in the address has a slash
                temp_list = filename[1:len(filename) - 1].split("/")
                # Adds file name to a file history list
                # Eliminates the first and last slash and splits the whole address into a list.
                current_dir = cd_location(temp_list[:len(temp_list) - 1], root_system)
                # Goes to the directory which the address is for.
            else:
                # No slash at the end
                temp_list = filename[1:].split("/")
                # Eliminates the last slash and splits the whole address into a list.
                current_dir = cd_location(temp_list[:len(temp_list) - 1], root_system)
                # Goes to the directory which the address is for.
            if current_dir != {}:
                # Ensure that the address is correct
                access_file(current_dir).append(temp_list[len(temp_list) - 1])
                file_list.append(temp_list[len(temp_list) - 1])
                # Adds file name to a file history list
                # Adds file name into the file list
            current_dir = old_pos
            # Goes back to the previous directory
        else:
            # No address given
            pos = access_file(current_dir)
            # Accesses file list in the directory
            pos.append(filename)
            # Adds file name into the file list
            file_list.append(filename)
            # Adds file name to a file history list


def rm(filename, current_dir, file_list):
    """
      This function deletes a file inside a directory
      :param filename: A string that holds the name of the file.
      :param current_dir: It is a dictionary which stores the current directory that the system is on.
      :return: None
      """
    current_file = []
    if filename == "":
        # Checks if file name is a space
        print("No file name specified.")
        # Outputs the message as space cannot be accepted as a file name.
    else:
        current_file = access_file(current_dir)
        # Accessing the file list inside the directory
        if filename in current_file:
            # Checks if file name entered by the user is inside the directory
            current_file.remove(filename)
            # Deletes the file inside the directory
            file_list.remove(filename)
        else:
            # Output the error message as the user entered a file name which is not inside the directory.
            print("No such file exits")


def rmdir(dir_name, current_dir):
    """
      This function deletes a directory inside a directory
      :param filename: A string that holds the name of the directory.
      :param current_dir: It is a dictionary which stores the current directory that the system is on.
      :return: None
      """

    temp_dir = {}
    temp_dir = access_directory(current_dir)
    # Accessing the directory dictionary inside the directory
    if dir_name == "":
        # Checks if directory name is a space
        print("No directory name specified")
        # Outputs the message as space cannot be accepted as a directory name.
    else:
        if dir_name in temp_dir:
            # Checks if directory name entered by the user is inside the directory
            del temp_dir[dir_name]
            # Deletes the directory inside the directory
        else:
            print("No such directory exists")
            # Output the error message as the user entered a directory name which is not
            # inside the directory.


def file_address_list(file_address):
    """
      This function splits the address into a list.
      :param file_address: A string that holds the file address with /.
      :return address_list: A list that holds the address without /.
    """
    address_list = []
    if file_address[0] != "/":
        address_list.append(file_address)
    else:
        address_list = file_address[1:].split("/")
    # Skips the first part of the file as it as an empty space
    # Adds the directory names into a list
    return address_list


def cd_location(address_list, root_system):
    """
      This function changes the directory when the full address is provided.
      :param root_system: A dictionary that holds all the directories and files.
      :param address_list: A list that holds the address without /.
      :return temp_dir: It is a dictionary which holds the current directory that the system is on.
      :return {}: Returns this when the wrong address of the dictionary is given by the user.
    """
    temp_dir = {}
    location = {}
    new_dir = {}
    old_pos = access_directory(root_system)
    # Accesses the directory
    for i in range(len(address_list)):
        if address_list[i] in old_pos:
            # Checks if the directory key is in the directory.
            temp_dir = old_pos[address_list[i]]
            # Moves to the next directory
        else:
            # Given an error message if there is no dictionary with that name.
            print("Wrong address of directory")
            return {}
            # Returns empty dictionary
        if i < (len(address_list) - 1):
            # Changes the directory until all the elements in the list are compared.
            new_dir = access_directory(temp_dir)
            # Accesses the new directory
            old_pos = new_dir
    return temp_dir


def pwd(history):
    """
      This function prints the complete address of the current directory
      :param history: A list that holds the complete path to the directory.
      :return temp_location: A string that holds the complete path to the directory with /.
    """
    temp_location = ''
    if history == []:
        # If history is empty, it means it is on the root_system.
        return ("/")
    else:
        temp_location = "/".join(history)
        # Joins the list with /s into a string.
        return ("/" + temp_location + "/")


def location_list(location, location_history, old_dir, current_dir):
    """
    This function makes a list which includes the complete path to a particular directory.
        :param location: It is a string that holds either the address to the directory
                       or just the directory names.
        :param old_dir: It is a dictionary that holds the current directory before the function begins.
        :param current_dir: It is a dictionary that holds the current or new directory.
        :param location_history: It is a list that holds the path to the directory.
        :return location_history: It is a list that holds the path to the directory.
    """
    count = len(location) - 1
    temp_history = []
    # Counts the number of element in the directory name.
    address_list = ""
    if location[0] == "/":
        # Checks if the location string has a /
        # / in the begining means it is a path.
        location_history = []
        temp_history = file_address_list(location)
        for address_list in temp_history:
            # Adds the whole path into the location_list
            location_history.append(address_list)
        return location_history

    else:
        if location not in location_history:
            # Adds the new directory name to the list when it is not present in the list.
            location_history.append(location)
        elif old_dir != current_dir:
            # Adds the new directory name to the list when both the current_dir and old_dir are not
            # equal.
            location_history.append(location)
        return location_history


def locate(filename, root_system, sub_name):
    """
    This function locates a file in the directories.
        :param filename: It is a string that holds the name of the file that is searched for
        :param root_system: A dictionary that holds all the directories and files.
        :param sub_name: It is a string that holds the complete address to the file
        :return: None
    """
    current_dir = {}
    current_dir = root_system
    flag = False
    if filename in access_file(current_dir):
        # Checks if file is in the directory.
        print("A file with that name was found at the following paths:")
        print("", end="\t\t")
        if sub_name == "":
            # If sub_name is empty which means that the file is in the root_system
            print("/" + filename)
        else:
            # Print the whole path to the file.
            print("/" + sub_name[:(len(sub_name) - 1)] + "/" + filename)
        flag = True
    for key in access_directory(current_dir):
        # Accesses every directory inside the directories
        sub_dir = access_directory(current_dir)[key]
        locate(filename, sub_dir, (sub_name + key + "/"))
        # Recursive statement to check each and every directory in the system.


def cd_back(current_dir, location_history, root_system):
    """
    This function goes back to the previous directory
        :param current_dir: It is a dictionary that holds the current or new directory.
        :param location_history: It is a list that holds the path to the directory.
        :param root_system: A dictionary that holds all the directories and files.
        :return current_dir: It is a dictionary that holds the current or new directory.
    """
    if location_history == []:
        # Checks if the current directory is on the root_system.
        current_dir = root_system
        # Stays on the root_system as it cannot go back.
    else:
        path = ""
        count = 0
        count = len(location_history) - 1
        location_history = location_history[:count]
        # Removes the last directory in the list.
        current_dir = cd_location(location_history, root_system)
        # Goes to the previous directory
    return current_dir


def ls_absolute(temp_string, current_dir, location_history):
    """
    This function is for the ls absolute function. It prints the contents of a directory
    when the full address is given.
        :param current_dir: It is a dictionary that holds the current or new directory.
        :param location_history: It is a list that holds the path to the directory.
    """

    temp_history = location_history
    count = len(temp_string) - 1
    old_dir = current_dir
    if temp_string[count] == "/":
        # Checks for whether the last element has a slash
        temp_string = temp_string[:count]
        # Removes last element
    current_dir = cd_location(file_address_list(temp_string), root_system)
    if current_dir != {}:
        # Adds the address to the location history list
        location_history = location_list(temp_string, location_history, old_dir, current_dir)
        ls_current(current_dir, location_history, root_system)
        # Uses ls main function to get the contents
    location_history = temp_history
    current_dir = old_dir
    # Replaces all the other values back to the previous


if __name__ == '__main__':
    while flag:
        # Loop to keep the user in the system
        entered_data = str(input("[cmsc201 proj3]$ "))
        # User entry
        user_input = entered_data.split(SPACED_STRING)
        # Splits the input into a list
        if user_input[ZERO] == MKDIR:
            # Checks for mkdir command
            if len(user_input) == SINGLE:
                # If only mkdir is entered, error message displayed
                print("No directory name specified")
            elif user_input[SINGLE] == "":
                print("Only space entered, nothing else")
            elif user_input[SINGLE] == "/":
                print("Only slash entered, nothing else")
            else:
                temp = user_input[SINGLE]
                mkdir(temp, current_dir)
                # Making a new directory
        elif user_input[ZERO] == CD:
            # Checks for CD command
            if len(user_input) == SINGLE or user_input[1] == EMPTY_STRING:
                # # If only cd is entered, error message displayed
                print("No directory name specified")
            elif user_input[SINGLE] == SINGLE_DOT:
                current_dir = current_dir
            else:
                temp_string = user_input[SINGLE]
                if user_input[SINGLE] == DOUBLE_DOT:
                    # Checks for cd ..
                    old_dir = current_dir
                    count = len(location_history) - SINGLE
                    current_dir = cd_back(current_dir, location_history, root_system)
                    if current_dir == {}:
                        # Directory on the root_system
                        current_dir = old_dir
                    if current_dir == access_directory(root_system):
                        location_history = []
                        # Resets location history as system is back to the root_system
                    else:
                        location_history = location_history[:count]
                    if current_dir == root_system:
                        location_history = []
                    if location_history == []:
                        current_dir = root_system
                elif temp_string[ZERO] != SLASH:
                    # Checks if input has a slash
                    old_dir = current_dir
                    current_dir = cd_current(user_input[SINGLE], current_dir)
                    # No slash, cd relative works
                    if current_dir == old_dir:
                        pass
                    else:
                        location_history = location_list(user_input[SINGLE], location_history, old_dir, current_dir)
                        # Adds the new directory to the location history list
                else:
                    if temp_string == SLASH:
                        # Checks if used entered only /
                        current_dir = root_system
                        location_history = []
                        # Goes back to the root_system with cd /
                    else:
                        count = len(temp_string) - SINGLE
                        old_dir = current_dir
                        if temp_string[count] == SLASH:
                            # Checks if first character in input has a slash,
                            temp_string = temp_string[:count]
                        current_dir = cd_location(file_address_list(temp_string), root_system)
                        # cd_absolute works
                        if current_dir != {}:
                            # Ensures that the address was correct
                            location_history = location_list(temp_string, location_history, old_dir, current_dir)
                            # adds the directory into the location history list
                        else:
                            current_dir = old_dir
                            # goes back to the previous directory if address given is wrong
        elif user_input[ZERO] == PWD:
            # Runs PWD function
            print(pwd(location_history))
        elif user_input[ZERO] == LS:
            # Runs ls function
            if len(user_input) == SINGLE:
                # Works for ls relative
                ls_current(current_dir, location_history, root_system)
            elif user_input[SINGLE] == "":
                print("Only space entered, nothing else")
            else:
                temp_history = location_history
                ls_absolute(user_input[SINGLE], current_dir, location_history)
                location_history = temp_history
                # Runs for ls absolute
        elif user_input[ZERO] == EXIT:
            # To exit the program
            if len(user_input) == SINGLE:
                flag = False
            else:
                # Nothing after exit is accepted
                print("Command not found: only exit")
        elif user_input[ZERO] == TOUCH:
            # Checks for touch function
            if len(user_input) == SINGLE:
                # Only touch command is written without the file name
                print("No file name specified")
            elif user_input[SINGLE] == "":
                print("Only space entered, nothing else")
            else:
                # Runs touch function
                touch(user_input[SINGLE], current_dir, root_system)
                # Adds file name to a file history list
        elif user_input[ZERO] == RM:
            # Checks for rm fucntion
            if len(user_input) == SINGLE:
                # If only rm is entered, error message displayed
                print("No file specified")
            else:
                # Runs rm function
                rm(user_input[SINGLE], current_dir, file_list)
        elif user_input[ZERO] == RMDIR:
            if len(user_input) == SINGLE:
                # If only rmdir is entered, error message displayed
                print("No file specified")
            else:
                # Runs rmdir function
                rmdir(user_input[SINGLE], current_dir)
        elif user_input[ZERO] == LOCATE:
            old_dir = current_dir
            if len(user_input) == SINGLE:
                # If only locate is entered, error message displayed
                print("No file specified")
            else:
                error_message = "No such file exists"
                count = ZERO
                filename = user_input[SINGLE]
                # Runs locate function
                (locate(filename, root_system, EMPTY_STRING))
                if filename not in file_list:
                    # Checks for whether file was in the system or not
                    print(error_message)
        else:
            # Prints this message when the command is not correctly typed
            print("Incorrect command, Type again")
