def is_array_odd(arr_test):

    if (len(arr_test) % 2) == 0:
        return False
    else:
        return True

def calc_median_index(arr_test):

    return int(((len(arr_test) + 1) / 2) - 1)

def get_user_cmds():
    return input("Who would you like to add to your team?\n")

test_arr = ['Giannis', 'BAM', 'Olajuwon', 'OG Anunoby', 'Josh Okogie']

msg = "We have a winner" if is_array_odd(test_arr) else "There's room for improvement"
print(msg)

print(calc_median_index(test_arr))

arr_roster = []
user_activity_detected = True

while user_activity_detected:

    chosen_user_cmd = get_user_cmds()

    if chosen_user_cmd in ['q', 'Q', 'quit', 'Quit']:
        print("\nIt's been a pleasure XD")
        user_activity_detected = False
    else:
        arr_roster.append(chosen_user_cmd)

print("You have chosen to include the following players in your team:\n")

i = 0
for player in arr_roster:
    print(f"{i + 1}. {player}")
    i += 1

if is_array_odd(arr_roster):
    resolved_median_index = calc_median_index(arr_roster)
    print(f"Your All Star MVP for team Nigeria is {arr_roster[resolved_median_index]}!!!")
else:
    print("The award has gone to the other squad :'(")
