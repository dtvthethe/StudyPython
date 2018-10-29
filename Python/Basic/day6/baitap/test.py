def fibonacci(number):
    return 0 if number == 0 else 1 if number == 1 else fibonacci(number-1) + fibonacci(number-2)

# for i in range(0, 10):
#     print(i, fibonacci(i))

from math import *

result = None
str_formula = 'sqrt((2*A*B)/C)'
values = [('A',5), ('B', 10), ('C', 7.5)]
for item in values:
    str_formula = str_formula.replace(item[0], str(item[1]))
str_cmmand = 'result = ' + str_formula
exec(str_cmmand)

print(result)
