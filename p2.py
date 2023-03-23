"""
File: p2.py
Author: Muhammad Umar
Date: 11/17/22
Lab Section: 43
Email:  mumar2@umbc.edu
Description:  This program tracks the student's attendance. The data is from a new card swipe system
in each classroom that tracks attendance. The data is stored in a file. Data from the file is extracted
and converted into a dictionary. It checks the number of students that attended the class on
a particular date. It returns the check in and check out time for all students.
It tells the names of the students who were late to class on every day. It finds the first student
who entered the class on a particular date.
"""


# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

# from dataEntryP2 import fillAttendanceData


# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!

def print_list(xlist):
    """
         This function prints the elements in the list. It prints each element on a different line.
          :param xlist: List of data that needs to be printed.
          :return: None
          """
    for element in xlist:
        print(element)


def connect_to_data_file(filename):
    """
      This function verifies whether the file that contains the date exists.
      :param filename: A string that holds the name of the file.
      :return infile: It holds the command of opening the file in reading mode.
      """
    # will return connection to data file
    infile = ""

    try:
        infile = open("rosters.txt", "r")
        infile = open("dataAllShow1stClass.txt", "r")
        infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file


def load_dictionary(attendance_file):
    """
      This function fetches data from a file and stores the data as a dictionary.
      :param attendance_file: It holds the command of opening the file in reading mode.
      :return attendance_dict: This is a dictionary which holds all the data regarding the students.
                          It holds the first and last names. It holds the check in time and date of
                          a student going to class.
      """
    data_0 = 0
    date_1 = 1
    date_2 = 2
    date_3 = 3
    line = []
    temp_data = ""
    temp_list = []
    attendance_dict = {}
    name = ''
    line = attendance_file.read()
    line = line.split('\n')
    # Splits the data in the file into a list.
    for i in range(len(line)):
        temp_data = line[i]
        temp_list = temp_data.split(", ")
        # Splits the data in the list into another list
        name = temp_list[data_0] + ", " + temp_list[date_1]
        # Join Last and First Name together
        time_and_date = temp_list[date_2] + ", " + temp_list[date_3]
        # Joins time and date together
        if name not in attendance_dict:
            attendance_dict[name] = []
            # checks if name is in the dictionary.
            # If it is not, then a new key in the dictionary is created which has the same name as name.
        attendance_dict[name].append(time_and_date)
        # Appends the values in the dictionary
    return attendance_dict


def load_roster(roster_file_name):
    """
      This function fetches data from a file and stores the data as a list.
      :param roster_file_name: It holds the name of the file in string.
      :return temp_list: This is a list which holds the first and last names of all the students
                         enrolled in the class.
      """
    line = []
    temp_data = ""
    temp_list = []
    attendance_dict = {}
    name = ''
    line = open(roster_file_name, "r")
    # opens the file in reading mode
    temp_data = line.read()
    temp_list = temp_data.split("\n")
    # Splits the data in the file into a list
    return temp_list


def print_dictionary(attend_dic):
    """
      This function prints the dictionary with its keys and values.
      :param attend_dic: This is a dictionary which holds all the data regarding the students.
                          It holds the first and last names. It holds the check in time and date of
                          a student going to class
      :return: None
      """
    for key in attend_dic:
        print(key, attend_dic[key])
        # Prints the data in this format: keys [values]


def display_attendance_data_for_student(student_name, attend_dic):
    """
          This function displays the complete data of a student.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class
          :param student_name: This is a string that holds the student's name.
          :return: None
    """
    attendance_data = []
    flag = False
    for key in attend_dic:
        if key == student_name:
            flag = True
            # Checks if key in the dictionary is equal to the student name entered by the user.
    if flag:
        # If they were equal, it extracts the values in the dictionary and prints it out.
        attendance_data = attend_dic[student_name]
        print(student_name, attendance_data)
        # Prints in the format key [values]
    else:
        # Prints this statement when they are not equal
        print("No student of this name in the attendance log")


def is_present(student_name, date, attend_dic):
    """
          This function checks if a student is present or not.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class
          :param student_name: This is a string that holds the student's name.
          :param date: This is a string that holds the date of the class.
          :return flag: This is a boolean that shows whether a student is present or not.
    """
    attendance_data = []
    flag = False
    temp_data = []
    list_value = []
    temp_value = ""
    if student_name in attend_dic:
        # Checks if the input data is in the dictionary.
        temp_data = attend_dic[student_name]
        # Stores the values in a list
        for i in range(len(temp_data)):
            temp_value = temp_data[i]
            list_value = temp_value.split(", ")
            # Splits the values into another list.
        for x in range(len(list_value)):
            if list_value[x] == date:
                # Checks if the data in the list is equal to the date
                flag = True
    else:
        # This happens when the input data is not in the dictionary
        flag = False
    return flag


def list_all_students_checked_in(date, attendance_dict):
    """
          This function checks the number of students checked in a particular date.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class
          :param date: This is a string that holds the date of the class.
          :return checked_in: This is a list that stores the number of students checked in a
                              particular date.
    """
    temp_value = []
    temp_value_1 = ''
    list_value_1 = []
    key = ""
    checked_in = []
    for key in attendance_dict:
        temp_value = attendance_dict[key]
        # Extracts the values in the dictionary using the key
        for i in range(len(temp_value)):
            temp_value_1 = temp_value[i]
            list_value_1 = temp_value_1.split(", ")
            # Splits the values into another list.
        for x in range(len(list_value_1)):
            if list_value_1[x] == date:
                # Checks if the data in the list is equal to the date
                checked_in.append(key)
                # Appends the data which has the same date.
    return checked_in


def print_count(result_data):
    """
          This function counts the number of elements in a list and prints the results.
          :param result_data: This is a list passed into the function
          :return: None
    """
    count = len(result_data)
    # Counts the number of elements in the list
    print(f"There were {count} records for this query")


def list_all_students_checked_in_before(date, time, attend_dict):
    """
          This function checks the number of students checked in a particular date before a particular
          time.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class
          :param date: This is a string that holds the date of the class.
          :param time: This is a string that holds the time of the class.
          :return checked_in_before: This is a list that stores the number of students checked in a
          particular date before a particular time.
    """
    checked_in_before = []
    temp_value = []
    temp_value_1 = ''
    list_value_1 = []
    key = ""
    flag = False
    for key in attend_dict:
        temp_value = attend_dict[key]
        # Stores the values in a list
        for i in range(len(temp_value)):
            temp_value_1 = temp_value[i]
            list_value_1 = temp_value_1.split(", ")
            # Splits the values into another list.
        for x in range(len(list_value_1)):
            if list_value_1[x] < date:
                # Check if the values are less than the date.
                flag = True
            if list_value_1[x] < time and flag:
                # Checks if value is less than time and flag is True
                checked_in_before.append(key)
                # Appends the key in the list.
    return checked_in_before


def list_students_attendance_count(days, attend_dict, full_roster):
    """
          This function displays the number of students that attend the classes for a number of days.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class.
          :param days: It is an integer that holds the number of days.
          :return both_student: This is a list that stores the number of students that attend the classes
                                  for a number of days.
    """
    temp_value = []
    temp_value_1 = ''
    list_value_1 = []
    key = ""
    both_student = []
    if days == 0:
        # It runs the function when there are 0 days
        return no_student(full_roster, attend_dict)
    else:
        for key in attend_dict:
            temp_value = attend_dict[key]
            # Stores the values in a list
            for i in range(len(temp_value)):
                temp_value_1 = temp_value[i]
                list_value_1 = temp_value_1.split(", ")
                # Splits the values into another list.
            if len(list_value_1) == days:
                # Checks if the length of the list is equal to the days entered by the user
                both_student.append(key)
        return both_student


def no_student(full_roster, attend_dict):
    """
          This function checks the number of students that attend none of the classes.
          :param attend_dic: This is a dictionary which holds all the data regarding the students.
                              It holds the first and last names. It holds the check in time and date of
                              a student going to class
          :return no_class: This is a list that stores the number of students that attend none of the
                            classes.
    """
    total_list = []
    key = ""
    total_data = ''
    flag = True
    no_class = []
    total_list = load_roster(full_roster)
    for total_data in total_list:
        flag = True
        # Stores the data of a list in a string variable
        for key in attend_dict:
            if total_data == key:
                # Checks if the data in the list is equal to the data in the dictionary. The names only
                flag = False
        if flag:
            no_class.append(total_data)
            # Appends the data if the names in the roster are not in the dictionary
    return no_class


def get_first_student_to_enter(date, attend_dict):
    """
      Simply, this function returns the student that swiped in first on a particular date.
      :param date: It holds the date of the class. It is a string.
      :param attend_dict: This is a dictionary which holds all the data regarding the students. It holds
                          first and last names. It holds the check in time and date of a student going
                          to class.
      :return first_temp: It is a string which stores the first and last name of the student who
                          arrived to the class first on a particular date.
      """
    data_1 = 1
    lowest_temp = ""
    temp_1 = ""
    key = ""
    index = ""
    temp_attendance_1 = ""
    attendance = []
    lowest_temp = "23:59:59"
    first_temp = ""
    list_attendance_1 = []
    for key in attend_dict:
        attendance = attend_dict[key]
        # Stores the values in a list
        for i in range(len(attendance)):
            temp_attendance_1 = attendance[i]
            list_attendance_1 = temp_attendance_1.split(", ")
            # Splits the values into another list.
            for x in range(len(list_attendance_1)):
                if list_attendance_1[x] == date:
                    # Checks if the values are equal to the data
                    if list_attendance_1[data_1] < lowest_temp:
                        # Checks if the time in the values is less than the lowest temperature
                        lowest_temp = list_attendance_1[data_1]
                        # Replaces the lowest temperature by the time in the value
                        index = key
                        # Replaces the lowest key
    first_temp = index
    return first_temp


if __name__ == '__main__':
    files = 'rosters.txt'
    infile = connect_to_data_file("dataAllShow1stAnd2ndClass.txt")
    if (infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    print_dictionary(data)

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    attended_both_class = list_students_attendance_count(2, data, files)
    print_list(attended_both_class)
    print_count(attended_both_class)

    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    attended_one_class = list_students_attendance_count(1, data, files)
    print_list(attended_one_class)
    print_count(attended_one_class)
    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    attended_no_class = list_students_attendance_count(0, data, files)
    print_list(attended_no_class)
    print_count(attended_no_class)
    print("**** First student to enter on 11/2/2022 ****")
    print(get_first_student_to_enter("11/2/2022", data))
    print("**** First student to enter on 11/3/2022 ****")
    print(get_first_student_to_enter("11/3/2022", data))
    print("**** First student to enter on 11/4/2022 ****")
    print(get_first_student_to_enter("11/4/2022", data))
    print("**** First student to enter on 11/5/2022 ****")
    print(get_first_student_to_enter("11/5/2022", data))
