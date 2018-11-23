class TaiLieu:
    def __init__(self, ma_tl='', ten_xb='', so_ban=0):
        self.ma_tl = ma_tl
        self.ten_xb = ten_xb
        self.so_ban = so_ban

    def __str__(self):
        return 'Ma:%s, NXB:%s, So ban:%d' % (self.ma_tl, self.ten_xb, self.so_ban)


class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, ten_tg='', so_trang=0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.ten_tg = ten_tg
        self.so_trang = so_trang

    def __str__(self):
        return super().__str__() + ', Ten tac gia:%s, So trang: %d' % (self.ten_tg, self.so_trang)


class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, so_ph=0, thang_ph=0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.so_ph = so_ph
        self.thang_ph = thang_ph

    def __str__(self):
        return super().__str__() + ', So phat hanh:%d, Thang phat hanh:%d' % (self.so_ph, self.thang_ph)


class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, ngay_ph=0):
        super().__init__(ma_tl, ten_xb, so_ban)
        self.ngay_ph = ngay_ph

    def __str__(self):
        return super().__str__() + ', Ngay phat hanh:%d' % (self.ngay_ph)
