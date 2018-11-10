from text_utility import read


class TaiLieu:
    def __init__(self, ma_tl='', ten_xb= '', so_ban= 0):
        self.ma_tl = ma_tl
        self.ten_xb = ten_xb
        self.so_ban = so_ban

    def __str__(self):
        return 'Ma:%s, NXB:%s, So ban:%d' %(self.ma_tl, self.ten_xb, self.so_ban)


class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_xb= '', so_ban= 0, ten_tg= '', so_trang= 0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.ten_tg = ten_tg
        self.so_trang = so_trang

    def __str__(self):
        return super().__str__() + ', Ten tac gia:%s, So trang: %d' %(self.ten_tg, self.so_trang)


class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_xb= '', so_ban= 0, so_ph= 0, thang_ph= 0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.so_ph = so_ph
        self.thang_ph = thang_ph

    def __str__(self):
        return super().__str__() + ', So phat hanh:%d, Thang phat hanh:%d' %(self.so_ph, self.thang_ph)


class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_xb= '', so_ban= 0, ngay_ph= 0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.ngay_ph = ngay_ph

    def __str__(self):
        return super().__str__() + ', Ngay phat hanh:%d' %(self.ngay_ph)


class QLTaiLieu:
    def __init__(self):
        self.ds_tai_lieu = []

    def nhap_tai_lieu(self):
        bl_next = 1

        while bl_next == 1:
            loai = int(input('Loại tài liệu(0:Sách/1:Tạp chí/2:Báo): '))
            ma_tl = str(input('Mã tài liêu: '))
            ten_xb = str(input('Tên xuất bản: '))
            so_ban = int(input('Số bản phát hành: '))
            if loai == 0:# Sách
                ten_tg = str(input('Ten tac gia: '))
                so_trang = int(input('Số trang: '))
                self.ds_tai_lieu.append(Sach(ma_tl, ten_xb, so_ban, ten_tg, so_trang))
            elif loai == 1: # Tạp chí
                so_ph = int(input('Số phát hành: '))
                thang_ph = int(input('Tháng phát hành: '))
                self.ds_tai_lieu.append(TapChi(ma_tl, ten_xb, so_ban, so_ph, thang_ph))
            elif loai == 2: #Báo
                ngay_ph = int(input('Ngày phát hành: '))
                self.ds_tai_lieu.append(Bao(ma_tl, ten_xb, so_ban, ngay_ph))
            bl_next = int(input('Nhap "1" de tiep tuc > '))


    def tao_dl_tu_dong(self, str_file_data):
        txt = read(str_file_data)
        for line in txt.split('\n'):
            arr_line = line.split(';')
            if arr_line[0] is '0': #Sach
                self.ds_tai_lieu.append(Sach(arr_line[1], arr_line[2], int(arr_line[3]), arr_line[4], int(arr_line[5])))
            elif arr_line[0] is '1': #Tap chi
                self.ds_tai_lieu.append(TapChi(arr_line[1], arr_line[2], int(arr_line[3]), int(arr_line[4]), int(arr_line[5])))
            elif arr_line[0] is '2': #Bao
                self.ds_tai_lieu.append(Bao(arr_line[1], arr_line[2], int(arr_line[3]), int(arr_line[4])))
            else:
                pass

    def hien_thi(self):
        for tl in self.ds_tai_lieu:
            print(tl.__str__())

    def tim_kiem(self, loai_tl):
        lst_filter = filter(lambda tl: tl.ma_tl.lower().startswith(loai_tl), self.ds_tai_lieu)
        for item in list(lst_filter):
            print(item.__str__())


qltl = QLTaiLieu()
# qltl.nhap_tai_lieu()
qltl.tao_dl_tu_dong('data_sample.txt')
qltl.hien_thi()
print('---------- Tìm kiếm theo loại ----------')
qltl.tim_kiem('tapchi')
