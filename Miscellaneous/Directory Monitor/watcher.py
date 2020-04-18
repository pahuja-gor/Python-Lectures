# https://www.thepythoncorner.com/2019/01/how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/
import os
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

import cacheManager
import configManager
import fileMover
import helper
# from watchdog.observers.polling import PollingObserver as Observer
import scanner

# from getpass import  getuser

if __name__ == '__main__':
    patterns = '*'
    ignore_patterns = ''
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(file):
    '''
    Prints out a statement when a new file is created in the specified directory


    :param file: The specified file
    :return: None
    '''
    # print(get_filename(file))
    print(f"{file.src_path} has been created!")


def on_deleted(file):
    '''
    Prints out a statement when a new file is deleted in the specified directory


    :param file: The specified file
    :return: None
    '''

    print(f"{file.src_path} has been deleted!")


def on_moved(file):
    '''
    Prints out a statement when a file is moved in and/or out of the specified directory


    :param file: The specified file
    :return: None
    '''

    print(f"{file.src_path} has been moved to {file.dest_path}!")


def on_modified(file):
    '''
    Prints out a statement when a file is modified in the specified directory.
    Moves the files to the 'source directory' after 'scanning' them
    Adds the filepaths of the 'processed' files to the 'cache.json' file


    :param file: The specified file
    :return: None
    '''

    # print(get_filename(file))
    print(f"{file.src_path} has been modified!")
    filepath = helper.get_filepath(file)
    caManager = cacheManager.cacheManager()
    if (caManager.check_if_processed(filepath) == False):
        print("Scanning")
        status = scanner.file_scan(file)
        print('Moving: ' + filepath)
        fileMover.move_to_directory(filepath, status)
        print('Adding')
        caManager.add_to_cache(filepath)
        print('Saving')
        caManager.save_file()
        print("saving to file")
        # print('File moved!')
    else:
        print('File already processed! File: ' + filepath)
        if (cfManager.retrieve_delete_duplicate_files() == True):
            if (os.path.exists(filepath)):
                print('ACTUALLY DELETING THE FILE!!!')
                os.remove(filepath)


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_moved = on_moved
my_event_handler.on_modified = on_modified

cfManager = configManager.configManager()

path = cfManager.retrieve_source_directory()
fileMover.create_directory(path)
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
my_observer.join()
