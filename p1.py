"""
File: p1.py
Author: Muhammad Umar
Date: 11/4/22
Lab Section: 43
Email:  mumar2@umbc.edu
Description: This program tracks the student's attendance. The data is from a new card swipe system
in each classroom that tracks attendance. It checks the number of students that attended class. It returns
the check in and check out time for all students. It tells the names of the students who were late. It
finds the first student who entered the class.
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''


def list_students_not_in_class(new_roster, new_data):
    """
        Compare the swipe log with the given course roster. Place those students that
        did not show up for class into a list.
        :param new_roster: It holds the first and last names of all the students enrolled into the class.
                            It is a list
        :param new_data: It holds all the check in and check out data of the students. It is a list
        :return absent_students: It holds all the students absent in the class. It is a list.
        """
    temp_name = []
    absent_students = []
    temp_attendance = []
    temp_second_name = ""
    temp_first_name = ""
    temp_first_attendance = ""
    temp = ""
    temp_second_attendance = ""
    x = 0
    i = 0
    for i in range(len(new_roster)):
        temp_name = new_roster[i]
        temp_name = temp_name.split(", ")
        flag = True
        temp_first_name = temp_name[1]
        temp_second_name = temp_name[0]
        for x in range(len(new_data)):
            temp_attendance = new_data[x]
            temp_attendance = temp_attendance.split(", ")
            temp_first_attendance = temp_attendance[1]
            temp_second_attendance = temp_attendance[0]
            if (temp_second_name == temp_second_attendance) and (temp_first_name == temp_first_attendance):
                flag = False
        if flag == True:
            temp = new_roster[i]
            absent_students.append(temp)
    return absent_students


def list_all_times_checking_in_and_out(new_roster, new_data):
    """
         Looking at the swiping log, this function will list all in and outs for a
         particular Student. Please note, as coded in the p1.py file given, this
         function was called three times with different student values.
         :param new_roster: It holds the first and last names of all the students enrolled into the class.
                            It is a list.
         :param new_data: It holds all the check in and check out data of the students. It is a list.
         :return check_status: It is a list which holds the data of a particular student's check in
                               check out time.
         """
    temp_name = []
    check_status = []
    temp_attendance = []
    temp_second_name = ""
    temp_first_name = ""
    temp_first_attendance = ""
    temp = ""
    temp_second_attendance = ""
    temp_check = ""
    temp_input = ""
    x = 0
    i = 0
    check = 0
    temp_name = new_roster.split(", ")
    temp_first_name = temp_name[1]
    temp_second_name = temp_name[0]
    for x in range(len(new_data)):
        temp_check = new_data[x]
        temp_attendance = temp_check.split(", ")
        temp_first_attendance = temp_attendance[1]
        temp_second_attendance = temp_attendance[0]
        if (temp_second_name == temp_second_attendance) and (temp_first_name == temp_first_attendance):
            check_status.append(temp_check)
    return check_status


def list_all_times_checked_in(new_data):
    """
           This function returns a list of when all student(s) FIRST swipe in.
           :param new_roster: It holds the first and last names of all the students enrolled into the class.
                            It is a list.
           :param new_data: It holds all the check in and check out data of the students. It is a list.
           :return check_in_time: It is a list which holds all the student's check in time and other data.

           """

    temp_1 = ""
    temp_2 = ""
    temp_data_1 = []
    temp_data_2 = []
    attendance_firstname_1 = ""
    attendance_firstname_2 = ""
    attendance_lastname_1 = ""
    attendance_lastname_2 = ""
    check_in_time = []
    counter = 0
    temp_3 = ""
    temp_data_3 = []
    for i in range(len(new_data)):
        temp_1 = new_data[i]
        temp_data_1 = temp_1.split(", ")
        attendance_firstname_1 = temp_data_1[1]
        attendance_lastname_1 = temp_data_1[0]
        for x in range(len(new_data)):
            flag = True
            temp_2 = new_data[x]
            temp_data_2 = temp_2.split(", ")
            attendance_firstname_2 = temp_data_2[1]
            attendance_lastname_2 = temp_data_2[0]
            for a in range(len(check_in_time)):
                if temp_2 == check_in_time[a] or temp_1 == check_in_time[a]:
                    flag = False
                temp_3 = check_in_time[a]
                temp_data_3 = temp_3.split(", ")
                if temp_data_3[0] == attendance_lastname_2 and temp_data_3[1] == attendance_firstname_2:
                    flag = False
                if temp_data_3[0] == attendance_lastname_1 and temp_data_3[1] == attendance_firstname_1:
                    flag = False
            if flag:
                if attendance_firstname_1 == attendance_firstname_2 and attendance_lastname_1 == attendance_lastname_2:
                    if temp_data_1[2] < temp_data_2[2] and temp_data_1[3] <= temp_data_2[3]:
                        check_in_time.append(temp_1)
                    elif temp_data_2[2] < temp_data_1[2] and temp_data_2[3] <= temp_data_1[3]:
                        check_in_time.append(temp_2)
                    else:
                        check_in_time.append(temp_2)
    return check_in_time


def fragmenting_time(time):
    """
      Converts the time in the format of HH:MM:SS into seconds.
      :param time: It is a string in the format of HH:MM:SS
      :return total_second: It is an integers which holds the total seconds.
      """
    split_time = []
    total_second = 0
    split_time = time.split(":")
    total_second = (int(split_time[0]) * 3600) + (int(split_time[1]) * 60) + int(split_time[2])
    return total_second


def list_students_late_to_class(late_time, attend_data):
    """
      When given a timestamp string and the swipe log, a list of those records
      of students who swiped in late into the class is produced. This function
      returns a list of when all student(s) FIRST swipe in.
      :param late_time: It is a string which is in the format of HH:MM:SS. It holds the boundary of the
                        late time. After this time, students are considered late.
      :param attend_data: It holds all the check in and check out data of the students. It is a list.
      :return late_students: It is a list which holds the data of all the students late.
      """
    new_data = list_all_times_checked_in(attend_data)
    total_time_entered = 0
    total_time_data = 0
    late_students = []
    temp = ""
    temp_input = ""
    temp_data = []
    late_temp = []
    late_data = ""
    total_time_entered = fragmenting_time(late_time)
    for i in range(len(new_data)):
        temp = new_data[i]
        temp_data = temp.split(", ")
        time_temp = temp_data[2]
        total_time_data = fragmenting_time(time_temp)
        if total_time_data >= total_time_entered:
            late_students.append(temp)
    return late_students


def get_first_student_to_enter(new_data):
    """
      Simply, this function returns the student that swiped in first. Note,
      the order of the data entered into the swipe log as not the earliest
      student to enter.
      :param new_data: It holds all the check in and check out data of the students. It is a list.
      :return first_temp: It is a string which stores the first and last name of the student who
                          arrived to the class first.
      """
    lowest_time = []
    lowest_temp = ""
    temp_time = []
    temp_1 = ""
    attendance = []
    temp_2 = ""
    temp_attendance_2 = []
    low_time = ""
    low_date = ""
    count = 0
    lowest_temp = new_data[0]
    temp_time = lowest_temp.split(", ")
    low_time = temp_time[2]
    low_date = temp_time[3]
    lowest_temp = new_data[0]
    temp_time = lowest_temp.split(", ")
    low_time = temp_time[2]
    low_date = temp_time[3]
    for i in range(len(new_data)):
        temp_1 = new_data[i]
        attendance = temp_1.split(", ")
        if low_date == attendance[3]:
            if low_time > attendance[2]:
                low_time = attendance[2]
                index = i
        elif low_date < attendance[3]:
            low_date = attendance[3]
            index = i
    first_temp = (new_data[index])
    first_temp = first_temp.split(", ")
    first_temp = first_temp[0] + ", " + first_temp[1]
    return first_temp


def printList(data_returned):
    """
       Simply prints the list. The function should not be able to change any
       values of that list passed in.
       :param data_returned: It is a list which contains data calculated from different functions.
       :return: None
       """
    for i in range(len(data_returned)):
        print(data_returned[i])


''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    

    # load class roster here into a list
    classRoster = fill_roster()

    # figure out which attendance data file to load here

    # load data
    attendData = fill_attendance_data()

    # use different tests
    # make sure roster was filled 
    # printList(classRoster)
    # make sure attendance data was loaded
    # printList(attendData)

    # list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    # list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    # display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    # display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    # display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
