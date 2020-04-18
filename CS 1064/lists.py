#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

#fibo_list = []
#fibo_list.append(0)
#fibo_list.append(1)
#for i in range(8): #in range(3,11):
#    fibo_list.append(fibo_list[-1] + fibo_list[-2])

#--------------------------------------------------------#

def negative_summation(number_list):
    list_sum = 0
    for i in range(len(number_list)): #0, 1, 2, 3, 4, 5, 6, ...
        if number_list[i] < 0:
            list_sum = list_sum + number_list[i]
    return list_sum

def negative_summation_better(number_list):
    list_sum = 0
    for item in number_list: # 1, 2, 3, 4, 5, -1, -2, -3, -4, 0
        if item < 0:
            list_sum = list_sum + number_list[i]
    return list_sum

print(negative_summation([1, 2, 3, 4, 5, -1, -2, -3, -4, 0]))
print(negative_summation([1, 2, 3, 4, 5]))

print(negative_summation_better([1, 2, 3, 4, 5]))

#--------------------------------------------------------#