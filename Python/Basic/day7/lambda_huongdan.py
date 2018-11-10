arr = [2, 8, 1, 2, 1, 9, 9, 4]

arr2 = map(lambda number: number * 2, arr)

print(list(arr2))

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

victims_sorted = sorted(victims, key=lambda item: item[1])

for item in list(victims_sorted):
    print(item)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
aa = filter(lambda x: x != 'X', garbled)
print(list(aa))
