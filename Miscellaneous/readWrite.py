# import os.path
# import sys

def open_file(filename, filepath):
    """
    Opens the file when given the filename and filepath of the file
    :param filename: The name of the file
    :param filepath: The path of the file
    :return: The 'opened' file
    """
    absolute_path = (filepath + "\\" + filename)
    file = open(absolute_path, 'a+')
    # if (os.path.exists(absolute_path)):
    #     file = open(absolute_path, 'a+')
    # else:
    #     print("The provided file path and/or provided filename doesn't exist!")
    #     sys.exit(-1)

    return file
    file.close()

def read_file(filename, filepath):
    '''
    Reads the data stored on the 'already opened' file
    :param filename: The name of the file
    :param filepath: The path of the file
    :return: None
    '''
    file = open_file(filename, filepath)
    file.seek(0)
    print(file.read())
    file.close()

def write_file(filename, filepath):
    '''
    Writes/Appends data to the 'already opened' file
    :param filename: The name of the file
    :param filepath: The path of the file
    :return: None
    '''
    file = open_file(filename, filepath)
    user_input = input("What would you like to write to this file? ")
    file.write(user_input)
    file.close()


if __name__ == '__main__':
    filename = input("What file would you like to open? ")
    filepath = input("Where is " + filename + " located? ")

    read_file(filename, filepath)
    write_file(filename, filepath)
    print("This is what the 'final draft' looks like: ")
    read_file(filename, filepath)