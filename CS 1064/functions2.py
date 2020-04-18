#Example 1

def multiply_values(x, y):
    product = x * y
    return (product)
print("multiply_values output: " + str(multiply_values(2, 3)))

#Example 2

def calculate_area_trapezoid(base1, base2, height):
    #(a+b)/2*h
    return ((base1 + base2)/(2*height))
area = calculate_area_trapezoid(1, 2, 1)
print("calculate_area_trapezoid output: ", area)

#Example 3

def i_am_from(home):
    return ("I am from " + home + ".")
print(i_am_from(input("Where are you from: ")))