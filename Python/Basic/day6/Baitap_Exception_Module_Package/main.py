from math import *
from homework6 import * 

str_path_text_file = 'fastfood_news.txt'

# Bai 1, trang 18:
print('Bai 1, trang 18:')
for i in range(0, 11):
    print(fibonacci(i), end=", ")

# Bai 2 a, trang 18
print('')
print('\nBai 2 a, trang 18:')
print('Tu xuat hien nhieu nhat trong file text: "%s"' %top_word_appear(str_path_text_file))


# Bai 2 b, trang 18
print('\nBai 2 b, trang 18:')
for item in list_word_counter(str_path_text_file, 'the'):
    print(item)

# Bai 3, trang 19
print('\nBai 3, trang 19:')
str_formula = 'sqrt((2*A*B)/C)'
values = [('A',5), ('B', 10), ('C', 7.5)]
try:
    result = None
    for item in values:
        str_formula = str_formula.replace(item[0], str(item[1]))
    exec('result = ' + str_formula)
    print(str_formula, '=' ,result)
except BaseException as ex:
    print(ex)