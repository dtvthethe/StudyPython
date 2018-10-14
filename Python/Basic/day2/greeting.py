import random

tap_cau_chao = ['Hello', 'Hi', 'Chao']
ten = 'Hung'
gioi = 'anh'
nam_sinh = 1994
hien_tai = [2018, 'Chó']

cau_chao = random.choice(tap_cau_chao)

tuoi = hien_tai[0] - nam_sinh
tuoi_tay = '%s tuổi' % tuoi

tap_du_lieu = ['Chuột', 'Trâu', 'Hổ', 'Mèo', 'Rồng', 'Rắn', 'Ngựa', 'Dê', 'Khỉ', 'Gà', 'Chó', 'Heo']
index_tuoi = (tap_du_lieu.index(hien_tai[1]) - tuoi) % 12

tuoi_ta = 'tuổi con %s' % tap_du_lieu[index_tuoi]

tuoi = random.choice([tuoi_tay, tuoi_ta])

loi_chao = '%s %s %s, %s %s à.' % (cau_chao, gioi, ten, gioi, tuoi)

print(loi_chao)

