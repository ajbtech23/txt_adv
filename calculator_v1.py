def calc_sum(x, y):
    return (x + y)

def calc_sub(x, y):
    return (x - y)

def calc_multiply(x, y):
    return (x * y)

def calc_divide(x, y):
    return (x / y)

def calc_powers(x, y):
    return (x ** y)

is_user_finished = False

while is_user_finished != True:

    user_decision = input("Would you like to do some math? Enter 'yes' to proceed\n")

    if user_decision == 'yes' or user_decision == 'YES':
        user_selected_calc = input("Choose a calculation to make: + or - or / or * or even **...\n")
        user_input_val_1 = int(input("Enter value 1: \n"))
        user_input_val_2 = int(input("Enter value 2: \n"))

        if user_selected_calc == "+":
            print(f"The sum of {user_input_val_1} and {user_input_val_2} is {str(calc_sum(user_input_val_1, user_input_val_2))}")
        elif user_selected_calc == '-':
            print(f"The difference between {user_input_val_1} and {user_input_val_2} is {str(calc_sub(user_input_val_1, user_input_val_2))}")
        elif user_selected_calc == "/":
            print(f"The result of dividing {user_input_val_1} by {user_input_val_2} is {str(calc_divide(user_input_val_1, user_input_val_2))}")
        elif user_selected_calc == "*":
            print(f"The produce of multiplying {user_input_val_1} and {user_input_val_2} is {str(calc_multiply(user_input_val_1, user_input_val_2))}")
        elif user_selected_calc == "**":
            print(f"The result of {user_input_val_1} to the power of {user_input_val_2} is {str(calc_powers(user_input_val_1, user_input_val_2))}")
        else:
            print("We could\'nt make sense of your input I\'m afraid...")
    else:
        is_user_finished = True
