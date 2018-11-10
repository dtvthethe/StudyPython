
class Nguoi:
    instances = 0
    def __init__(self):
        self.ten = 'Nguyen Van A'
        self.tuoi = 20
        self.vo_chong = None

    def __str__(self):
        return '%s:%s đã cưới %s' % (self.ten, self.tuoi, self.vo_chong)

    def __len__(self):
        return self.tuoi

    def cuoi(self, ten):
        self.vo_chong = ten

hoc_vien_1 = Nguoi()
Nguoi.instances +=1
hoc_vien_1.ten = 'Nghia'
hoc_vien_1.tuoi = 28
hoc_vien_1.cuoi('Trâm')

hoc_vien_2 = Nguoi()
Nguoi.instances +=1
hoc_vien_2.ten = 'Thắng'
hoc_vien_2.tuoi = 27

print(hoc_vien_1)
print(hoc_vien_2)
print(hoc_vien_1.__class__.instances)

del hoc_vien_1
Nguoi.instances -=1

print(hoc_vien_2.__class__.instances)



