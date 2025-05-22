user_input_message = "Add number of days, and conversion units: \n"

def days_to_units(number_of_days, conversion_unit):
    conversion_result = "Unsupported units"

    if conversion_unit == "Hours":
        conversion_result = f"{number_of_days} days are {number_of_days * 24} {conversion_unit}"
    elif conversion_unit == "Minutes":
        conversion_result = f"{number_of_days} days are {number_of_days * 24 * 60} {conversion_unit}"
    return conversion_result


'''
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            units_result = days_to_units(user_input_number)
            print(units_result)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
    else:
        print("enter an int numb nuts")
'''

def validate_and_execute(user_input_dictionary):
    try:
        user_input_number = int(user_input_dictionary["Days"])

        # logic to validate if the input is a positive integer
        if user_input_number > 0:
            units_result = days_to_units(user_input_number, user_input_dictionary["Units"])
            print(units_result)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a valid positive number")
    except ValueError:
        print("enter an int numb nuts")
