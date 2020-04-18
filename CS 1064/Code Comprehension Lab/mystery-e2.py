# TODO:
# 1. Write documentation for the function -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, add extra documentation within the function if necessary
#     2.1. In this case, the logical structure of the code can be simplified, in addition to updating the names of variables and the function.  
#          Make sure that any changes you make to the logic don't break the test cases!

def is_Equal(x, xx, xxx):

  """Returns a boolean that evaulates whether the three arguments are equal to each other or not

  Arguments:
    x: int
    xx: int
    xxx: int
  Returns:
    True or False: bool
  """

  # TODO: can this logic be simplified?
  if (x == xx and x == xxx and xx == xxx and xxx == x and xxx == xx):
    return True
  return False

  #Original Code
  '''if x == xx:
    if x == xxx:
      if xx == xxx:
        if xxx == x:
          if xxx == xx:
            return True
  return False'''






# Don't edit anything below this point; these are the test cases  
assert( is_Equal(True, True, False) == False )
assert( is_Equal(False, False, False) == True )
assert( is_Equal(1, 0, 1.1) == False )
assert( is_Equal(9/9, 2 - 1, 1.0) == True )
print("All tests passed")
