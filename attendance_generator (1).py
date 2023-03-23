from datetime import datetime, time, date, timedelta
import random
import csv


def read_names_csv(file_name):
    new_male_names = {}
    new_female_names = {}
    new_family_names = {}
    with open(file_name) as csv_file:
        names_reader = csv.DictReader(csv_file)
        male_name_header, male_count_header, female_name_header, female_count_header, family_name_header, family_count_header = names_reader.fieldnames
        for line in names_reader:
            new_male_names[line[male_name_header].capitalize()] = int(line[male_count_header])
            new_female_names[line[female_name_header].capitalize()] = int(line[female_count_header])
            new_family_names[line[family_name_header].capitalize()] = int(line[family_count_header])

    return new_male_names, new_female_names, new_family_names


def get_int_input(prompt, default_value=None, **keyword_params):
    result = None
    while result is None:
        try:
            result = int(input(prompt))
        except ValueError:
            if default_value is not None:
                return default_value
            print('You must enter an integer value.')
    return result


def get_float_input(prompt, default_value=None, **keyword_params):
    result = None
    while result is None:
        try:
            result = float(input(prompt))
        except ValueError:
            if default_value is not None:
                return default_value
            print('You must enter an floating point value.')
    return result


def generate_class_days(num_days, starting_date_string, day_string):
    starting_date = date.fromisoformat(starting_date_string)
    day_codes = {day: i for i, day in enumerate(['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])}
    class_days = []
    for code in day_codes:
        if code in day_string:
            class_days.append(day_codes[code])
    if not class_days:
        class_days = [0, 2]  # monday, wednesday for no reason other than they screwed up the day choices

    current_day = starting_date
    day_list = []
    while len(day_list) < num_days:
        if current_day.weekday() in class_days:
            day_list.append(current_day)
        current_day += timedelta(days=1)
    return day_list


def generate_students(num_students, male_names, female_names, family_names):
    student_names = []

    male_name_list = []
    male_name_weights = []
    female_name_list = []
    female_name_weights = []
    family_name_list = []
    family_name_weights = []

    for male_name, weight in male_names.items():
        male_name_list.append(male_name)
        male_name_weights.append(weight)
    for female_name, weight in female_names.items():
        female_name_list.append(female_name)
        female_name_weights.append(weight)
    for family_name, weight in family_names.items():
        family_name_list.append(family_name)
        family_name_weights.append(weight)

    for _ in range(num_students):
        if random.random() < 0.5:
            first_name = random.choices(male_name_list, male_name_weights, k=1)[0]
        else:
            first_name = random.choices(female_name_list, female_name_weights, k=1)[0]
        last_name = random.choices(family_name_list, family_name_weights, k=1)[0]

        student_names.append(f'{last_name}, {first_name}')
    return student_names


def generate_roster(roster_name, student_names):
    if roster_name in ['rosters.txt', 'dataAllShow1stAnd2ndClass.txt', 'dataAllShow1stClass.txt', "p2.py", "dataEntryP2.py", "attendance_generator.py"]:
        raise ValueError("Do not overwrite the original roster, called rosters.txt or any of the original files")
    with open(roster_name, 'w') as roster_file:
        for i, name in enumerate(student_names):
            if i < len(student_names) - 1:
                roster_file.write(f'{name}\n')
            else:
                roster_file.write(f'{name}')


def generate_attendance_data(attendance_file_name, class_days, roster_names, probability_of_attendance=0.8, start_time_string='09:00:00'):
    if attendance_file_name in ['rosters.txt', 'dataAllShow1stAnd2ndClass.txt', 'dataAllShow1stClass.txt', "p2.py", "dataEntryP2.py", "attendance_generator.py"]:
        raise ValueError("Do not overwrite the original roster, called rosters.txt or any of the original files")
    write_lines = []
    start_time = datetime.strptime(start_time_string, '%H:%M:%S')
    with open(attendance_file_name, 'w') as attendance_file:
        for day in class_days:
            current_roster_names = list(roster_names)
            random.shuffle(current_roster_names)
            for student in current_roster_names:
                if random.random() < probability_of_attendance:
                    seconds_difference = int(random.normalvariate(0, 300))
                    student_time = start_time + timedelta(seconds=seconds_difference)
                    write_lines.append(f'{student}, {student_time.strftime("%H:%M:%S")}, {day.strftime("%m/%d/%Y")}')

        for i, line in enumerate(write_lines):
            if i < len(write_lines) - 1:
                attendance_file.write(f'{line}\n')
            else:
                attendance_file.write(f'{line}')


if __name__ == '__main__':
    try:
        the_male_names, the_female_names, the_family_names = read_names_csv('names.csv')
        print('names loaded successfully')
        seed = input('Would you like to set a random seed, enter the seed or return to skip: ')

        random.seed(seed)

        num_days = get_int_input('How many days of class would you like to simulate? ')
        starting_date = input('Enter the starting date in the format here: YYYY-MM-DD: ')
        date_types = input('Which days would you like, type Mo Tu We Th Fr Sa Su for the days')
        the_class_days = generate_class_days(num_days, starting_date, date_types)

        num_students = get_int_input('How many students would you like? ')
        names_of_students = generate_students(num_students, the_male_names, the_female_names, the_family_names)
        roster_file_name = input('What is the roster file name? ')
        generate_roster(roster_file_name, names_of_students)
        print('Roster file generated.')
        attendance_file_name = input('What is the attendance file name? ')

        prob_of_att = get_float_input('What is the probability that a student attends a given class? (Defaults to 95%)', 0.95)
        generate_attendance_data(attendance_file_name, the_class_days, names_of_students, prob_of_att)
        print('Attendance file generated.')

    except FileNotFoundError:
        print('Names file was not found.')

