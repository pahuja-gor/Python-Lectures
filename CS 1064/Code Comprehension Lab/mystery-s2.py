# TODO:
# 1. Write documentation for the function -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

def multiply_list(x):
    """Returns the product of all of the values in the array

    Arguments:
      x: int (array)

    Returns:
      product: int that represents the product of all of the values in the array
    """

    if x == []:
        return 0
    else:
        product = 1
        for i in x:
            product *= i
        return product

		
		
		
		
		
# Don't edit anything below this point; these are the test cases		
a = [0,1,3,5]
b = [-1,3,6,23,-9]
c = [-1,-3,-5]
d = [0]
e = []

assert(multiply_list(a) == 0)
assert(multiply_list(b) == 3726)
assert(multiply_list(c) == -15)
assert(multiply_list(e) == 0)
print("All tests passed")
