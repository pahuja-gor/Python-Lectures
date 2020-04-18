# TODO:
# 1. Write documentation for the function -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

######
# FAQ
######
#
#   Q: What does the * mean in the call to mystery(*a_list) ?
#   A: This is the "splat" operator. It unpacks / "spreads out" a list or tuple
#      into its individual components for functions that take named arguments instead
#      of lists/tuples.
#      See https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

def sort_list(x, xxx, xxxxx, xxxx, xx):
  """Returns the list with its values sorted in ascending order

  Arguments:
    x: int
    xx: int
    xxx: int
    xxxx: int
    xxxxx: int
  Returns:
    [x, xx, xxx, xxxx, xxxxx]: array that is sorted numerically in ascending order
  """

  args = [x, xxx, xxxxx, xxxx, xx]
  return sorted(args)[0]

  
  
  
  
  
  
# Don't edit anything below this point; these are the test cases  
a_list = [0,0,0,0,0]
assert(sort_list(*a_list) == 0)
a_list = [1,0,0,0,0]
assert(sort_list(*a_list) == 0)
a_list = [1, 2, 3, 3, 2]
assert(sort_list(*a_list) == 1)
a_list = [5, 3, 4, 5, 4]
assert(sort_list(*a_list) == 3)
print("All tests passed")
