class TaiLieu:
    def __init__(self, ma_tl='', ten_nxb='', so_ban_phat_hanh=0):
        self.ma_tl = ma_tl
        self.ten_nxb = ten_nxb
        self.so_ban_phat_hanh = so_ban_phat_hanh


class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban_phat_hanh=0, ten_tag_gia='', so_trang=0):
        super().__init__(self, ma_tl, ten_nxb, so_ban_phat_hanh)

        self.ten_tag_gia = ten_tag_gia
        self.so_trang = so_trang


class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban_phat_hanh=0, so_phat_hanh=0, thang_phat_hanh=1):
        super().__init__(self, ma_tl, ten_nxb, so_ban_phat_hanh)

        self.so_phat_hanh = so_phat_hanh
        self.thang_phat_hanh = thang_phat_hanh


class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban_phat_hanh=0, ngay_phat_hanh='1/1/1990'):
        super().__init__(ma_tl, ten_nxb, so_ban_phat_hanh)

        self.ngay_phat_hanh = ngay_phat_hanh


class QuanLyTaiLieu:

    def __init(self):
        self.ds_tai_lieu = []

    def nhap_thong_tin(self):
        sach_1 = Sach('sach001', 'NXB Kim Dong', 3, 'Tac gia abc', 120)
        sach_2 = Sach('sach002', 'NXB GD', 7, 'Tac gia XYZ', 42)
        tai_lieu_1 = TaiLieu('tailieu001', 'NXB Kim Dong', 3, )
        tai_lieu_2 = Sach('tailieu002', 'NXB Kim Dong', 3, 'Tac gia abc', 120)
        bao_1 = Sach('sach001', 'NXB Kim Dong', 3, 'Tac gia abc', 120)