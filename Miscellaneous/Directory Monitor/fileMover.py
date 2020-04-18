import os
import shutil

import configManager


def create_directory(filepath):
    '''
    Creates the directory/folder if it doesn't exist


    :param filepath: The path of the folder/directory
    :return: None
    '''
    if not os.path.exists(filepath):
        os.makedirs(filepath)


def move_to_directory(filepath, status):
    '''
    Moves the file to the intended directory based on its category


    :param filepath: The filepath of the file
    :param status: The status of the file
    :return: None
    '''

    cfManager = configManager.configManager()

    clean_directory = cfManager.retrieve_clean_directory()
    sus_directory = cfManager.retrieve_suspicious_directory()
    pot_mal_directory = cfManager.retrieve_potential_malicious_directory()
    mal_directory = cfManager.retrieve_malicious_directory()

    filename_with_ext = filepath[filepath.rindex("\\") + 1:]

    if not os.path.exists(filepath):
        return

    if (status == 'Clean'):
        create_directory(clean_directory)
        # create_directory(filepath)
        shutil.move(filepath,
                    clean_directory + filename_with_ext)
    elif (status == 'Suspicious'):
        create_directory(sus_directory)
        # create_directory(filepath)
        shutil.move(filepath,
                    sus_directory + filename_with_ext)
    elif (status == 'Potential Malicious'):
        create_directory(pot_mal_directory)
        # create_directory(filepath)
        shutil.move(filepath,
                    pot_mal_directory + filename_with_ext)
    elif (status == 'Malicious'):
        create_directory(mal_directory)
        # create_directory(filepath)
        shutil.move(filepath,
                    mal_directory + filename_with_ext)
