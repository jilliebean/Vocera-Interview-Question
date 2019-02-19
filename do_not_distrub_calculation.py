from datetime import (
    datetime
)

# global constants
name_index = 3
dnd_index = 2
time_index = 1
date_index = 0
dnd_true_list = []
dnd_true = "DND true"
dnd_false = "DND false"


def openFile(filename):
    f = open(filename, 'r')
    if f.mode == 'r':
        for line in f.readlines():
            line = line.strip()
            find_dnd_times(line.split(','))


def find_dnd_times(list_employee):
    global name_index
    global dnd_index
    global time_index
    global date_index
    global dnd_true
    global dnd_false
    global dnd_true_list

    if not is_in_list(list_employee[name_index], dnd_true_list):
        if list_employee[dnd_index] == dnd_true:
            dnd_true_list.append(list_employee)
        else:
            raise Exception("Cannot have false state before true state")
    else:
        if list_employee[dnd_index] == dnd_false:
            subtract_times(list_employee, dnd_true_list)


def is_in_list(name, list):
    global name_index

    for entry in list:
        if name == entry[name_index]:
            return True
    return False


def subtract_times(list_employee, dnd_true_list):
    global name_index
    global dnd_index
    global time_index
    global date_index
    global dnd_true
    global dnd_false

    for entry in dnd_true_list:
        if list_employee[name_index] == entry[name_index]:
            time_in_dnd = get_time_range(list_employee, entry)
            format_time_in_dnd(list_employee[name_index], time_in_dnd)


def get_time_range(list_employee, dnd_true_list):
    global time_index
    global date_index

    start_time = datetime.strptime(dnd_true_list[date_index] + " " +
                                   dnd_true_list[time_index],
                                   "%m/%d/%y %H:%M:%S")
    end_time = datetime.strptime(dnd_true_list[date_index] + " " +
                                 list_employee[time_index],
                                 "%m/%d/%y %H:%M:%S")
    return end_time - start_time


def format_time_in_dnd(name, time_in_dnd):
    time_in_dnd = str(time_in_dnd)
    time_in_dnd = time_in_dnd.strip('0:')
    time_in_dnd = time_in_dnd.strip('00:')

    if len(time_in_dnd) == 3:
        print(name + " " + time_in_dnd[0] + "hours" + time_in_dnd[1]
              + "minutes" + time_in_dnd[2] + "seconds")
    elif len(time_in_dnd) == 2:
        print(name + " " + time_in_dnd[0] + "minutes" + time_in_dnd[1]
              + "seconds")
    else:
        print(name + " " + time_in_dnd[0] + " seconds")


def main():
    file_contents = openFile("employee_timestamps.txt")


main()
