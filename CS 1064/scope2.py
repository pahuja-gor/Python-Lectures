def a_function():
    a = 12         # <-- local a
    print(a)       # <-- prints 12
    return a       # <-- returns 12
    
a = 7              # <-- global a
a_function()       # <-- doesn't capture return value
print(a)           # <-- prints 7
a = a_function()   # <-- does capture return value
print(a)           # <-- prints 12



########### Number guess example ##############################

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
    else:
        print("That was terrible.")
        
my_number = generate_number()     # <-- my_number is global
my_guess = get_input()            # <-- my_guess is global
is_correct(my_number, my_guess)

### Definition Lookup Example ###

def lookup(definition_component):
    this_class = "Incredibly awesome place where I get to spend a Friday"
    
    if definition_component in this_class:
        return "this_class"
    elif definition_component in cat:
        return "cat"
    elif definition_component in ta:
        return "ta"
    elif definition_component in VT:
        return "VT"
    else:
        return "no word found"

def i_hate_everything():
    this_class = "Lame thing that I need to do on Friday"
    ta = "I can't find them"

#Global Variables
this_class = "An awesome place where you learn about Python"
cat = "Furry lovable creature that sleeps too much"
ta = "Very helpful individual and you should visit their office hours"
VT = "Overpopulated"

print("The definition of VT is: " + VT)
i_hate_everything()
print(lookup("need"))
