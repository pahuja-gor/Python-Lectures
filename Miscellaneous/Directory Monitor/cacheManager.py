import json

import configManager


class cacheManager:
    cache_files = []

    def __init__(self):
        cfManager = configManager.configManager()
        with open(cfManager.retrieve_cache_directory()) as cache_file:
            self.cache_files = json.load(cache_file)

    def check_if_processed(self, filepath):
        '''
        Checks whether the file at the specified filepath has been processed or not


        :param filepath: The filepath of the specified file
        :return: A bool that specifies if a file has been processed
        '''
        processed_files = self.cache_files["PROCESSED_FILES"]
        # unprocessed_files = jsonAnalyzer.retrieve_unprocessed_files()
        # filepath = helper.get_filepath(filepath)

        if (filepath in processed_files):
            return True
        else:
            return False

    def add_to_cache(self, filepath):
        '''
        Adds the file at the specified filepath to the 'cache.json' file


        :param filepath: The filepath of the specified file
        :return: None
        '''
        processed_files = self.cache_files["PROCESSED_FILES"]
        processed_files.append(filepath)

    def save_file(self):
        '''
        Saves the 'processed' files in the 'cache.json' file


        :return: None
        '''
        cfManager = configManager.configManager()
        cache_file_path = cfManager.retrieve_cache_directory()
        # if datetime.datetime.now() >= (self.last_saved_time(cache_file_path) + datetime.timedelta(seconds=30)):
        with open(cache_file_path, 'w') as json_file:
            print("Saving to: ")
            print(self.cache_files)
            json.dump(self.cache_files, json_file, ensure_ascii=False, indent=5)
            # json.dump(self.cache_files)

    # def last_saved_time(self, filepath):
    #     return time.ctime(os.path.getmtime(filepath))
    #     return datetime.datetime.now()
