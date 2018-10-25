file = None

def init(file_path):
    global file
    file = open(file_path)


def close():
    pass
FILE_PATH = 'data.txt'
def read():
    file = open(FILE_PATH)
    lines = file.read()
    file.close()
    return lines

def write():
    pass

def count_by_lines():
    pass

def count_by_words():
    pass

def count_by_chars():
    pass
def erase():
    pass
