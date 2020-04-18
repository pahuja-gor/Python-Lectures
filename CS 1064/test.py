# # def create_it(s):
# #    d = {}
# #    for c in s:
# #        if c.lower() not in d:
# #            d[c.lower()] = 1
# #        else:
# #            d[c.lower()] += 1
# #    return d
# # def print_it(d):
# #    for key in d:
# #        print(key + ": " + str(d[key]))
# # print_it(create_it(input("Enter a word: ")))
#
# # import random
# # computersNumber = random.randint(1,100)
# # userInput = 0
# # while computersNumber != userInput:
# #     userInput = int(input("Enter a number: "))
# #     if computersNumber < userInput:
# #         print("Your guess was too high!")
# #     elif computersNumber > userInput:
# #         print("Your guess was too low!")
# # print("Yay you're right!")
# #
# # user_input = int(input("Hopefully this loop quits! "))
# # while (user_input > 0):
# #     user_input -= 1
# #     print("infinite loops aren't fun")
# # print("phew, successfully exited")
#
# #def filter_high (numbers):
# #    #new_list = []
# #    for num in numbers:
# #        if num > 50:
# #            numbers.remove(num)
# #    return numbers
# #print(filter_high([30, 40, 50, 60, 70]))
# #
# #def filter_high2 (nums):
# #    new_list = nums
# #    for num in nums:
# #        if num > 50:
# #            new_list.remove(num)
# #    return new_list
# #print(filter_high2([30, 40, 50, 60, 70]))
# #
# # def front_back(str):
# #   if (len(str) == 1):
# #       return str
# #   else:
# #       return (str[len(str) - 1] + str[1:len(str) - 1] + str[0])
# # print(front_back("code"))
# # print(front_back("a"))
# # print(front_back("ab"))
#
# str = 'example@gmail.com'
# print(str.__contains__('@'))
# print(str.find('@'))
# if (str[str.find('@'):] == '@gmail.com'):
#     print('Found')
#
# import threading
#
#
# def gfg():
#     print("GeeksforGeeks\n")
#
#
# timer = threading.Timer(2.0, gfg)
# timer.start()
# print("Exit\n")

# x = 9
# y = 4
# def func(a):
#     return a + x
# print(func(y) + x)

# y = 42
# def foo():
#     global x
#     x = 17
#     def bar():
#         x = 99
#     bar()
# foo()
# print(x)

# x = range(7)
# for i in x:
#     print(i)
#
# x = 10
# var = x + 5
# while var:
#     var -= 1
#     print('var: ', var)
#
# from string import ascii_lowercase
# print(ascii_lowercase)
# alphachars = []
# for char in list(ascii_lowercase):
#     alphachars.append(char)
# alphachars.remove('q')
# print((alphachars))
# alphachars = "".join(alphachars)
# print(alphachars)

import colorama

# print(colorama.Style.BRIGHT + "hey")
print(colorama.Fore.RED + 'some red text')
print(colorama.Back.GREEN + 'and with a green background')
print(colorama.Style.DIM + 'and in dim text')
print(colorama.Style.RESET_ALL)
print('back to normal now')