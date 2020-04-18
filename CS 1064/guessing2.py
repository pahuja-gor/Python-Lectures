import random

# Function 1: generate a random number between 1 and 10
def generate_number():
    number = random.randint(1,10)    # <-- number is local to the function
    return number

# Function 2:  get user's guess
def get_input():
    guess = input("Guess a number (1-10): ")   # <-- guess is local to the function
    return int(guess)          # <-- input() returns a string, but we need an integer

# Function 3:  check to see if we guessed the right number
def is_correct(number, guess):    # <-- number and guess are both local to the function
    if number == guess:
        print("Yay you're so smart!")
        return True
    else:
        print("That was terrible.")
        return False

def find_max(list_of_guesses):
    if list_of_guesses == []:
        return None
    biggest_thing = list_of_guesses[0]
    for guess in list_of_guesses:
        if guess > biggest_thing:
            biggest_thing = guess
    return biggest_thing

def main():
    guesses = []
    for counter in range(5):
        print ("You have " + str(5 - counter) + " guesses left!")
        my_number = generate_number()     # <-- my_number is local
        my_guess = get_input()            # <-- my_guess is local
        guesses.append(my_guess)
        print("The number was: " + str(my_number))
        is_correct(my_number, my_guess)
        did_we_win = is_correct(my_number, my_number)
        if did_we_win:
            break
    print("Your guesses were: ")
    print(guesses)
    print("Your biggest guess was: " + str(find_max(guesses)))

main()