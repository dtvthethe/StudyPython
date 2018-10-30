import re
from collections import Counter
from text_utility import read


def fibonacci(number):
    '''
    Fibonacci 
    :param number: Number term to calculate
    :return: Fibonacci's number from term of number computed
    '''
    return 0 if number == 0 else 1 if number == 1 else fibonacci(number-1) + fibonacci(number-2)


def top_word_appear(str_path_file_text):
    '''
    Word is the most appear inside text file
    :param str_path_file_text: text path file
    :return: A Word is the most appear inside text file
    '''
    try:
        return Counter(read(str_path_file_text).split()).most_common(1)[0][0]
    except:
        return None

def list_word_counter(str_path_file_text, keyword):
    '''
    List of words that are appear after the keyword inside text file
    :param str_path_file_text: text path file
    :param keyword: keyword
    :return: List of words that are appear after the keyword inside text file
    '''
    try:
        lst = []
        lst_by_key = re.findall(keyword+'\s\S+', read(str_path_file_text))
        for item in Counter(lst_by_key).items():
            lst.append((item[0].split()[1], item[1]))
        return lst
    except:
        return None