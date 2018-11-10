def read(str_path_file):
    """
    Read all text from text file
    :param str_path_file: Text file path to read
    :return: All text in your text file
    """
    file = None
    try:
        file = open(str_path_file, 'r')
        text = file.read()
    except:
        text = None
    finally:
        if file is not None: file.close()
    return text

def write(str_path_file, text_content):
    """
    Write content to text file
    :param str_path_file: Text file path to write
    :param text_content: Content text to write
    """
    file = None
    try:
        file = open(str_path_file, 'w')
        file.write(text_content)
    except:
        pass
    finally:
        if file is not None: file.close()


def count_by_lines(str_path_file):
    """
    Number of lines in your text file
    :param str_path_file: Text file path to count by lines
    :return: Number of lines
    """
    return len(read(str_path_file).split('\n'))


def count_by_words(str_path_file):
    """
    Number of words in your text file
    :param str_path_file: Text file path to count by words
    :return: Number of words
    """
    return len(read(str_path_file).split())


def count_by_chars(str_path_file):
    """
    Number of characters in your text file
    :param str_path_file: Text file path to count by characters
    :return: Number of characters
    """
    return len(read(str_path_file))


def erase(str_path_file):
    """
    Delete content in your text file
    :param str_path_file: Text file path to delete
    """
    write(str_path_file, '')