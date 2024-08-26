def say_hello(name):
    print("Say hello to the bad guy ==> " + name)

say_hello("Anthony Soprano")

answer = input("Would you like another greeting?\n")
if answer == 'y' or answer == 'yes':
    say_hello("Johnny Sack")
else:
    print("Bugger off then...")
