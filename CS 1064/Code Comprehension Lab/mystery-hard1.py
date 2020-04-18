# TODO:
# 1. Write documentation for the function -- what does it do, what is the input meaning and type, what is the output meaning and type
# 2. Make any changes needed for readability -- update variable names, update function names, 
#    add extra documentation within the function if necessary
#       2.1. The logical structure of the code does not need to be changed; only the variable/function names and the documentation

def list_equals_array(x, y):
    '''Checks to see whether the values in the list equal the values in the array.
        In other words, the function checks to see if the list and array contain the same values.

        Arguments:
          x: List
          y: Array
        Returns:
          bool : Returns whether the list is equal to the array (True) or not (False)'''

    for a, b in x:
        assert (a in y)
        assert (b == y[a])


# Don't edit anything below this point; these are the test cases
l = [
    ['cow', 'moo'],
    ['duck', 'quack'],
    ['sheep', 'baa'],
    ['cat', 'meow'],
    ['dog', 'bark']
]

d = {
    'cow': 'moo',
    'duck': 'quack',
    'sheep': 'baa',
    'cat': 'meow',
    'dog': 'bark'
}

list_equals_array(l, d)
print('Tests passed')
