my_number = int(input("Guess a nunber (1-10: "))

if my_number < 0:
    print("You can't give us a negative number!")
elif my_number == 0:
    print("You can't guess zero!")
elif my_number > 0:
    print("You number is way too large!")
else:
    print("Your number is valid")