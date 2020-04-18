def get_filepath(file):
    '''
    Returns the file's filepath


    :param file: The specified file
    :return: The file's filepath
    '''
    return file.src_path


def get_filename(file):
    '''
    Returns the file's filename


    :param file: The specified file
    :return: The file's filename
    '''
    filename = file.src_path[file.src_path.rindex("\\") + 1: file.src_path.find('.') - len(file.src_path)]
    return filename


def get_extension(file):
    '''
    Returns the file's extension


    :param file: The specified file
    :return: The file's extension
    '''
    file_extension = file.src_path[file.src_path.rindex('.') - len(file.src_path):]
    return file_extension


def get_filename_with_extension(file):
    '''
    Returns the file's filename with the extension


    :param file: The specified file
    :return: The file's extension
    '''
    filename_with_ext = file.src_path[file.src_path.rindex("\\") + 1:]
    # print(filename_with_ext)
    return filename_with_ext
