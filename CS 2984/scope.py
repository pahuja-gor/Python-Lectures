a = 2
# b = 12
# c = 8

def a_function(d):
    a = 10
    def b_function():
        a = 42
        global c
        c = 1700
        b = 3

        def c_function(c):
            d = 24
            print(a, b, c, d) # 42 3 62 24
        c_function(62)

        print(a, b, c, d) # 42 3 1700 89

    b_function()
    global b
    b = 11
    print(a, b, c, d) # 10 11 1700  89

a_function(89)
print(a, b, c) # 2 11 1700