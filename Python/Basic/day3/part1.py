input = '[12, 25, 38, 18, 16]'

def is_list_type():
    lst = []
    try:
        exec('lst = ' + input)
        if isinstance(lst, list): # if type(lst) == type(list())
            return True
        else:
            return False
    except Exception as a:
        return False

print(is_list_type())