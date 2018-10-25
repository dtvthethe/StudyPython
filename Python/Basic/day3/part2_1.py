import random
from operator import itemgetter

victims = [('1', 18, 'nam'),
           ('2', 23, 'nữ'),
           ('3', 23, 'nữ'),
           ('4', 23, 'nam'),
           ('5', 23, 'nam'),
           ('6', 65, 'nam'),
           ('7', 62, 'nữ'),
           ('8', 8, 'chó'),
           ('9 Doo', 8, 'chó'),
           ('10', 6, 'nam'),
           ('11', 12, 'nữ')]


def my_sort_func(item):
    if item[2] == 'chó':
        return 500 + item[1]
    if item[1] <= 15:
        return -1000 + item[1]
    if item[1] >= 60:
        return -500 + item[1]
    if item[2] == 'nam':
        return 1000 + item[1]

    return item[1]

lst = sorted(victims, key=my_sort_func, reverse=False)


random.shuffle()

for item in lst:
    print(item)
