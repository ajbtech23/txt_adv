favorites = []

more_items = True

while more_items:
    user_input = input("What more would you like to add to your growing cart?\n")

    if user_input in ['q', 'Q', 'Quit', 'quit']:
        print("Thank you for choosing to shop with us - goodbye :D\n")
        more_items = False
    else:
        print(f"You've chosen to buy {user_input} - great choice!")
        favorites.append(user_input)

for i in range(len(favorites)):
    print(f"{i + 1}. {favorites[i]}")

arr_fresh_goods = []

is_user_still_shopping = True

def get_user_selection():
    return input("\nWhat would you like to chuck into the cart today?\n")

while is_user_still_shopping:
    user_selection = get_user_selection()

    if user_selection == "":
        print("We'd like to say ty for shopping with us today - goodbye :D")
        is_user_still_shopping = False
    else:
        print(f"Excellent choice! The {user_selection} is a crowd favourite as of late!")
        arr_fresh_goods.append(user_selection)

for i in range(len(arr_fresh_goods)):
    print(f"{i + 1}. {arr_fresh_goods[i]}")

for good in arr_fresh_goods:
    print(f"* {good}")


print("There's always something...")
