import json


def read2(str_path_file):
    """
    Read all data from json file
    :param str_path_file: Data file path to read
    :return: All data in your JSON file
    """
    json_file = None
    try:
        json_file = open(str_path_file, 'r')
        json_data = json.load(json_file)
    except:
        json_data = []
    finally:
        if json_file is not None: json_file.close()
    return json_data


def write2(str_path_file, content):
    """
    Write content to json file
    :param str_path_file: JSON file path to write
    :param content: Content to write JSON file
    """
    json_file = None
    try:
        json_file = open(str_path_file, 'w')
        json.dump(content, json_file, indent=4, separators=(',', ': '))
    except:
        pass
    finally:
        if json_file is not None: json_file.close()
