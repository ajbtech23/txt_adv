def pretty_print_unordered(to_print):
    i = 1
    for item in to_print:
        print(f"{i}* " + str(item))
        i += 1

    for i in range(len(to_print)): # Len first gives you the absolute value scalar size of the array e.g. 5; and then range creates a zero based index arr with 5 elements [0, 1, 2, 3, 4]
        print(str(i + 1) + ". " + str(to_print[i]))


favorites = []
more_items = True

while more_items:
    user_input = input("Enter something you like: \n")
    if user_input == "":
        more_items = False
    else:
        favorites.append(user_input)

print("Here all of the the things you like: \n")
pretty_print_unordered(favorites)
