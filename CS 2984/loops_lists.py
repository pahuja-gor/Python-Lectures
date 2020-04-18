import time

# def rFactorial(target):
#     if target == 1:
#         return 1
#     else:
#         return target * rFactorial(target - 1)
#
# def iFactorial(target):
#     value = 1
#     for i in range(1, target+1):
#         value *= 1
#     return value
#
# startRFactorial = time.time_ns()
# for i in range(1000):
#     rFactorial(50)
# # print(rFactorial(100))
# endRFactorial = time.time_ns()
# runtimeRFactorial = endRFactorial - startRFactorial
#
# startIFactorial = time.time_ns()
# for i in range(1000):
#     iFactorial(50)
# # print(iFactorial(100))
# endIFactorial = time.time_ns()
# runtimeIFactorial = endIFactorial - startIFactorial
#
# print("Recursive:", runtimeRFactorial)
# print("Iterative:", runtimeIFactorial)

####################################################################

old_list = [-3, -2, -1, 0, 1, 2, 3]
no_negatives = [item for item in old_list if item >= 0]
print(no_negatives)