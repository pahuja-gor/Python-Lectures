# TODO:
# 1. Write documentation for the functions -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

def maximum(x, y, z):
    """Returns the largest integer out of the 3 arguments, in other words,
    this function returns the maximum value out of three 3 integers

    Arguments:
      x: int
      y: int
      z: int

    Returns:
      max: The largest number out of the three arguments
    """

    # assert ensures that x, y, and z are different
    assert(x != y and x != z and y != z)

    max = x
    for elem in [x, y, z]:
        if elem > max:
            max = elem
    return max

def middle_num(x, y, z):
    """Sorts the three arguments from least to greatest and then
    returns the middle value (i.e. second number from the list) from the list

    Arguments:
      x: int
      y: int
      z: int

    Returns:
      int: The second number from the list
    """

    # assert ensures that x, y, and z are different
    assert(x != y and x != z and y != z)
    
    mystery_list = [x, y, z]

    mystery_list.sort()

    return mystery_list[1]

def minimum(x, y, z):
    """Returns the lowest number out of the three arguments

    Arguments:
      x: int
      y: int
      z: int

    Returns:
      int: The lowest number out of the three arguments
    """

    # assert ensures that x, y, and z are different
    assert(x != y and x != z and y != z)

    m_1 = maximum(x, y, z)

    m_2 = middle_num(x, y, z)

    for elem in [x, y, z]:
        if elem != m_1 and elem != m_2:
            return elem

            
            
            
            
            
# Don't edit anything below this point; these are the test cases            
assert( minimum(1, 2, 3) == 1 )
assert( minimum(3, 2, 1) == 1 )
assert( minimum(5, 2, 9) == 2 )
print("All tests passed")
