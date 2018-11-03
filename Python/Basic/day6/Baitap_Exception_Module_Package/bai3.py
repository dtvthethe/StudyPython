import math

bt = '5 ^ B + 100 - B + √(3 + C)'
param = [('A', 1), ('B', 2), ('C', 3)]
result = None
for item in param:
    bt = bt.replace(item[0], str(item[1]))
bt = bt.replace('^','**')
bt = bt.replace('√','math.sqrt')
exec('result = ' + bt)
print(result)