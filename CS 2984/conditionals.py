import math

switcher = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten"
}

# user_input = int(input("Give me a number from 0-10: "))
# print(switcher[user_input])
#
# def sqr(x):
#     return math.pow(x, 2)
#
# function_switcher = {
#     "str" : str,
#     "int" : int,
#     "abs" : abs,
#     "sqr" : sqr
# }
#
# user_function = input("Give me a function" + f" ({function_switcher.keys()}): ")
# print(function_switcher[user_function](user_input))
#######################################################################################################################

# def factorial(x):
#     # base case
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)

def fibonacci(x):
    if x == 0 or x == 1:
        # print(x)
        return x
    else:
        # print(fibonacci(x - 2) + fibonacci(x - 1))
        return fibonacci(x - 2) + fibonacci(x - 1)

print(fibonacci(100))
# print(factorial(1000))