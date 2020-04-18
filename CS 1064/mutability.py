#IMMUTABLE: strings, integers, booleans, floats, NoneType

my_string = "this is a string"
my_string = my_string.upper()
my_string = my_string.replace(" ", "!")

my_integer = 7
my_integer = my_integer + 3

#MUTABLE: lists

my_list = [1,2,3,4]
my_list.append(5)
my_List = my_list.append(6) # = None

my_string = "this is a string"
for char in my_string:
    if char == " ":
        print("I found a space!")

my_csv_list = "42,65,-17,0,41"
for datapoint in my_csv_list.split(","):
    print(int(datapoint))
    
my_sep_list = ['a', 'b', 'c']
the_whole_string = " comes before ".join(my_sep_list)