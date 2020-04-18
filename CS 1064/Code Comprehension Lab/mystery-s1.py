# TODO:
# 1. Write documentation for the function -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

def sum_list(a_list):
    """Returns an int that represents the sum of all of the values in a list

    Arguments:
      a_list: List
    Returns:
      sum : int (The sum of all of the values in a list)
    """

    sum = 0
    for element in a_list:
        sum = sum + element
    return sum

	
	
	
# Don't edit anything below this point; these are the test cases	
a_list = []
assert(sum_list(a_list) == 0)
a_list = [1]
assert(sum_list(a_list) == 1)
a_list = [1,2]
assert(sum_list(a_list) == 3)
print("All tests passed")
