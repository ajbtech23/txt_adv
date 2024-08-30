def pretty_print_unordered(arr):
    for element in arr:
        element = str(element) + " is a much needed addition to the team"
        print("* " + element)

def pretty_print_ordered(arr):
    i = 0
    for element in arr:
        element = f"At the {i + 1} we have " + str(element) + " who is a much needed addition to the team!"
        print(element)
        i += 1

def pretty_print_ordered_range_way(arr):
    for i in range(len(arr)):
        print(f"At the {i + 1} we have {arr[i]} - the reigning MVP!")


arr_roster = []
more_players = True

while more_players:
    user_selection = input("Who would you like to add to your team?\n")

    if user_selection == "":
        print("Thanks for playing XD\n")
        more_players = False
    else:
        arr_roster.append(user_selection)

pretty_print_unordered(arr_roster)
print("")
pretty_print_ordered(arr_roster)
print("")
pretty_print_ordered_range_way(arr_roster)
