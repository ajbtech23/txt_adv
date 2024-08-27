# This code will calculate the median index within an array
# And then return the median value associated with said index
# The only caveat is that the array must contain an odd number of elements

def get_user_input():
    return input("What would you like to add to your growing list?\n")

def is_total_goods_odd(arr):

    if ((len(arr) % 2) == 0):
        return False
    else:
        return True

def calc_median_index(arr):

    return int(((len(arr) + 1)/2) - 1)

def play():

    arr_user_goods = []
    is_user_still_active = True

    print("Welcome to Size? in Carnaby Street; it's time to shop :D")

    while is_user_still_active:

        user_selection = get_user_input()

        if user_selection in ['q', 'Q', 'quit', 'Quit']:
            print("\nWe appreciate you for choosing to shop with us today")
            print("See you next time :D\n")
            is_user_still_active = False
        else:
            arr_user_goods.append(user_selection)

    for good in arr_user_goods:
        print(f"You have chosen to acquire: {good}")

    print("\nAs part of a special promotion we are running we will give you 1 item from your purchase for free XD")
    print("Which item do you ask? Why, the middle one of course?\n")

    if is_total_goods_odd(arr_user_goods):

        median_index = calc_median_index(arr_user_goods)
        print(f"Congratulations! We will be giving you the {arr_user_goods[median_index]} for free XD")

    else:
        print("Because you had an even no. of shoes in your basket we can't enter you into the promotion :'(")
        print("Soz m8 - try again next time!!!")




play()
