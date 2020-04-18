import random

# Function 1: Generate a random number between 1 and 10
def generate_number():
    number = random.randint(1,10)
    return number


# Function 2: Get user's guess
def get_input():
    guess = input("Guess a number (1-10): ")
    return int(guess)


# Function 3: Check to see if we guessed the right number
def is_correct(number, guess):
    if number == guess:
        print("Congratulations! You are smart!")
    else:
        print("You're not smart!")
        
my_number = generate_number()
my_guess = get_input()
is_correct(my_number, my_guess)