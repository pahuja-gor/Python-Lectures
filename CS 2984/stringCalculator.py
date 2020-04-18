def string_calculator(str):
    if (str == ""):
        return 0
    my_numbers = str.split(',')
    sum = 0
    for num in my_numbers:
        sum += int(num)
    return sum


def main():
    testSingleNumber()
    testEmptyString()
    testTwoNumbers()
    testAddingZero()
    testFiveInputs()
    testNegativeNumbers()
    print('all tests passed')

#######################################

def testSingleNumber():
    assert string_calculator("7") == 7, "single number doesn't return itself"


def testEmptyString():
    assert string_calculator("") == 0, "empty string doesn't produce 0"


def testTwoNumbers():
    assert string_calculator("1,2") == 3, "1+2 != 3"


def testAddingZero():
    assert string_calculator("1,0") == 1, "1+0 != 1"


def testFiveInputs():
    assert string_calculator("1,2,3,4,5") == 15, "1+2+3+4+5 != 15"


def testNegativeNumbers():
    assert string_calculator("1,-2") == -1, "1+(-2) != -1"


main()