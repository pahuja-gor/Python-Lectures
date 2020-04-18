# numbers = [1, 2, 3]
# booleans = [True, False, False]
# letters = ['a', 'b', 'c']
#
# numbers_set = {1, 2, 3}
# letters_set = {'a', 'b', 'c'}
#
# zipped = zip(numbers_set, letters_set)
# print(list(zipped))
# print(set('abcdea'))
####################################################
# x = [[31, 17],
#      [40, 51],
#      [13, 12]]
#
# print(x)
# print('\n')
# print(list(zip(*x)))
####################################################
# def aFunction():
#     pass
# print(aFunction)
####################################################
# def applyFunction(data, func):
#     result = []
#     for item in data:
#         result.append(func(item))
#     return result
# myData = [1, -2, -5, 6.2]
#
# def sqr(num):
#     return num ** 2
#
# my_functions = [abs, int, sqr]
#
# print(applyFunction(myData, abs))
# print(applyFunction(myData, int))
# print(applyFunction(myData, sqr))
#
# for function in my_functions:
#     print(applyFunction(myData, function))

# def myFunction(A=[]):
#     A.append(42)
#     return A
#
# print(myFunction())
# print(myFunction())
# print(myFunction())