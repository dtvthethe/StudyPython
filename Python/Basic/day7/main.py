class Nguoi:
    def __init__(self, ten):
        self.tuoi = 0
        self.ten = ten


class HocVien(Nguoi):
    def __init__(self, ten, tuoi, lop):
        super(HocVien, self).__init__(ten)
        self.lop = lop
        self.tuoi = 1


hv = HocVien('Nam', 23, 'Py')

print(hv.ten, hv.tuoi, hv.lop)