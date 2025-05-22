from helper import validate_and_execute, user_input_message
from math import ceil, floor

user_input = ""
''' Adding a comment to main '''

while user_input != "exit":
    user_input = input(user_input_message)
    user_input_list = user_input.split(":")
    user_input_dictionary = {"Days": user_input_list[0], "Units": user_input_list[1]}
    validate_and_execute(user_input_dictionary)