# TODO:
# 1. Update the documentation for the function -- does this function actually do what the documentation describes, 
#    what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

def absolute_value(x):
  """Returns absolute value of x if x is greater than or equal to 0

  Arguments:
    x: int (must be greater than or equal to 0)
  Returns:
    abs(x)
  """
  assert(x >= 0)
  return abs(x)

  
  
  
  
# Don't edit anything below this point; these are the test cases  
assert(absolute_value(0) == 0)
assert(absolute_value(1) == 1)
print("All 'tests' passed")
