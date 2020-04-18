import configManager
import helper


def file_scan(file):
    '''
    Classifies the specified file into one of four groups:
        -Malicious
        -Potential Malicious
        -Suspicious
        -Clean


    :param file: The file
    :return: The group that the file will be classified into
    '''

    # filepath = helper.get_filepath(file)
    # print(filepath)
    cfManager = configManager.configManager()

    suspicious_extensions = cfManager.retrieve_suspicious_extensions()
    potential_malicious_extensions = cfManager.retrieve_potential_malicious_extensions()
    malicious_extensions = cfManager.retrieve_malicious_extensions()

    if (helper.get_extension(file) in malicious_extensions):
        # print('Mal' + filepath)
        return 'Malicious'
    elif (helper.get_extension(file) in potential_malicious_extensions):
        # print('Pot' + filepath)
        return 'Potential Malicious'
    elif (helper.get_extension(file) in suspicious_extensions):
        # print('Sus' + filepath)
        return 'Suspicious'
    else:
        # print('Clean' + filepath)
        return 'Clean'
