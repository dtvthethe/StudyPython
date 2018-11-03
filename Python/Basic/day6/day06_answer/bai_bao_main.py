# input
bai_bao_file = open('bai_bao.txt', 'r')

#code

# Tạo từ điển word với key là word, value là số lần xuất hiện (số lượng)
dem_tu_dict = {}
for line in bai_bao_file.readlines():
    # line = <class 'str'>:'Cho đến nay, đã ...'

    ds_word = line.strip().rsplit()
    # ds_word = <class 'list'>: ['Cho', 'đến', 'nay,', 'đã', ...]'

    for word in ds_word:
        if word in dem_tu_dict:
            dem_tu_dict[word] += 1
        else:
            dem_tu_dict[word] = 1

# {'Cho': 1, 'đến': 1, 'nay,': 2, 'đã': 6, 'có': 12, 'nhiều': 3 ...

word = ''
max_w = 0
for key, val in dem_tu_dict.items():
    if val > max_w:
        max_w = val
        word = key

print(word, max_w)



tu_nhieu_nhat = ''

# output
print(tu_nhieu_nhat)
bai_bao_file.close()