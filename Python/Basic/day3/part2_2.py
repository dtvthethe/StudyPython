dict_nums = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy',
             '8': 'tám', '9': 'chín'}
dict_class = ('trăm', 'nghìn', 'triệu', 'tỉ')
dict_tens = {'0': '', '1': 'mốt', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám',
             '9': 'chín'}
str_ten = 'mười'
str_le = 'linh'
str_muoi = 'mươi'

def doc_mot_so(str_num):
    return dict_nums[str_num]


def doc_hai_so(str_num):
    if int(str_num) < 20:
        if int(str_num) == 11:
            return '%s %s' % (str_ten, doc_mot_so('1'))
        else:
            return '%s %s' % (str_ten, dict_tens[str_num[1]])
    else:
        return '%s %s %s' % (doc_mot_so(str_num[0]), str_muoi, dict_tens[str_num[1]])


def doc_ba_so(str_num):
    str_read = '%s %s' % (doc_mot_so(str_num[0]), dict_class[0])
    if int(str_num) % 100 == 0:
        return str_read
    else:
        if int(str_num[1]) == 0:
            return '%s %s %s' % (str_read, str_le, doc_mot_so(str_num[2]))
        return '%s %s' % (str_read, doc_hai_so(str_num[1:]))


def tach_lop(str_num):
    if len(str_num) <= 3:
        return [str_num]
    else:
        lst = []
        for x in range(len(str_num), 0, -3):
            if x - 3 < 0:
                lst.append(str_num[0: x])
            else:
                lst.append(str_num[x - 3: x])
        lst.reverse()
        return lst


def doc_so_hang_tram(str_num):
    if len(str_num) == 1:
        return doc_mot_so(str_num)
    elif len(str_num) == 2:
        return doc_hai_so(str_num)
    else:
        return doc_ba_so(str_num)


def doc_so(str_num):
  arr = tach_lop(str_num)
  stri = ''
  for index, item in enumerate(arr):
    if index == len(arr) - 1:
      stri += doc_so_hang_tram(item)
    else:
      stri += doc_so_hang_tram(item) + ' ' + dict_class[len(arr) - 1 - index] + ' '
  return stri


# stri = '12345678902894' # 12 345 678 902 894
stri = '15678902894' #  8 902 894

print(doc_so(stri))
