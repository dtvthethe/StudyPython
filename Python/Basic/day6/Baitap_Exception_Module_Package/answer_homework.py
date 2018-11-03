
bai_bao_file = open('fastfood_news.txt', 'r')

lines = bai_bao_file.readlines()
my_dict = dict()

for line in lines:
    for word in line.split():
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

max = 0
tu_nhieu_nhat = ''

for key, value in my_dict.items():
    if value > max:
        tu_nhieu_nhat = key
        max = value
# print(tu_nhieu_nhat)
# print(max)

if 'the' in my_dict:
    print(my_dict['the'])
else:
    print(None)