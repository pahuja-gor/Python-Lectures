import json
from getpass import getuser


# from pprint import pprint

class configManager:
    config_properties = {}

    def __init__(self):
        with open("config.json") as json_file:
            self.config_properties = json.load(json_file)

    def retrieve_source_directory(self):
        '''
        Returns the 'source directory' that will be monitored for filesystem changes


        :return: The source directory
        '''
        return self.config_properties["WATCH_DIRECTORY"].replace("\\username\\", f"\\{getuser()}\\")

    def retrieve_clean_directory(self):
        '''
        Returns the path of the folder that contains the 'clean files'


        :return: The 'Clean' folder's filepath
        '''
        return self.config_properties["CLEAN_FOLDER"].replace("\\username\\", f"\\{getuser()}\\")

    def retrieve_suspicious_directory(self):
        '''
        Returns the path of the folder that contains the 'suspicious files'


        :return: The 'Suspicious' folder's filepath
        '''
        return self.config_properties["SUSPICIOUS_FOLDER"].replace("\\username\\", f"\\{getuser()}\\")

    def retrieve_potential_malicious_directory(self):
        '''
        Returns the path of the folder that contains the 'potentially malicious files'


        :return: The 'Potential Malicious' folder's filepath
        '''
        return self.config_properties["POTENTIAL_MALICIOUS_FOLDER"].replace("\\username\\", f"\\{getuser()}\\")

    def retrieve_malicious_directory(self):
        '''
        Returns the path of the folder that contains the 'malicious files'


        :return: The 'Malicious' folder's filepath
        '''
        return self.config_properties["MALICIOUS_FOLDER"].replace("\\username\\", f"\\{getuser()}\\")

    def retrieve_suspicious_extensions(self):
        '''
        Returns the file extensions that are considered 'suspicious files'


        :return: A list of file extensions
        '''
        return self.config_properties["SUSPICIOUS_EXTENSIONS"]

    def retrieve_potential_malicious_extensions(self):
        '''
        Returns the file extensions that are considered 'potentially malicious files'


        :return: A list of file extensions
        '''
        return self.config_properties["POTENTIAL_MALICIOUS_EXTENSIONS"]

    def retrieve_malicious_extensions(self):
        '''
        Returns the file extensions that are considered 'malicious files'


        :return: A list of file extensions
        '''
        return self.config_properties["MALICIOUS_EXTENSIONS"]

    def retrieve_cache_directory(self):
        '''
        Returns the filepath of the 'cache.json' file


        :return: The filepath of the JSON file
        '''
        return self.config_properties["CACHE_JSON_FILEPATH"]

    def retrieve_delete_duplicate_files(self):
        '''
        Returns the boolean value specifying whether duplicate files should be deleted or not


        :return: A bool specifying if duplicate files should be deleted
        '''
        return self.config_properties["DELETE_DUPLICATE_FILES"]

# print(retrieve_source_directory())
# print(retrieve_clean_directory())
# print(retrieve_suspicious_directory())
# print(retrieve_potential_malicious_directory())
# print(retrieve_malicious_directory())
