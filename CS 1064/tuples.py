percentages = (95, 90, 97, 87, 1)
print(percentages[0]) # Prints 95
a, b, c, d, e = percentages

def return_two_things():
    a = input("Give me the first thing!")
    b = input("Give me the second thing")
    return (a,b)

(var1, var2) = return_two_things()
my_tuple = (1, 2, 4, [4, 5], 'cat')
my_tuple[3].append(6)
print(my_tuple)
my_tuple[3].remove(4)
print(my_tuple)