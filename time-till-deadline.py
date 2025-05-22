from datetime import datetime

# Learn Python:06/06/2025

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = datetime.strptime(input_list[1], "%d/%m/%Y")
print(input_list)
print(goal)
print(deadline)

days_till_deadline = str(deadline - datetime.now()).split(",")
print(f"Time remaining for your goal of {goal} is: {days_till_deadline[0]} ")