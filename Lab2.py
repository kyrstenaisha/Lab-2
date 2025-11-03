print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(temperature_list):
    total = sum(temperature_list)
    count = len(temperature_list)
    avg = total / count
    return float(avg)

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for value in string_list:
        float_list.append(float(value.strip())) 
    return float_list

def find_min_max(temperature_list):
    minimum = min(temperature_list)
    maximum = max(temperature_list)

    return [int(minimum), int(maximum)]

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")
