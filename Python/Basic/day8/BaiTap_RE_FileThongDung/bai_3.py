from json_utility import write2, read2
from export_utility import export_to_excel
from enum import Enum


class TypeOfDoc(Enum):
    SACH = 1
    TAP_CHI = 2
    BAO = 3


class TaiLieu:
    def __init__(self, doc_type=TypeOfDoc.SACH.value, ma_tl='', ten_xb='', so_ban=0):
        self.doc_type = doc_type
        self.ma_tl = ma_tl
        self.ten_xb = ten_xb
        self.so_ban = so_ban

    def __str__(self):
        return 'Ma:%s, NXB:%s, So ban:%d' % (self.ma_tl, self.ten_xb, self.so_ban)


class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, ten_tg='', so_trang=0):
        super().__init__(TypeOfDoc.SACH.value, ma_tl, ten_xb, so_ban)
        self.ten_tg = ten_tg
        self.so_trang = so_trang

    def __str__(self):
        return super().__str__() + ', Ten tac gia:%s, So trang: %d' % (self.ten_tg, self.so_trang)


class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, so_ph=0, thang_ph=0):
        super().__init__(TypeOfDoc.TAP_CHI.value, ma_tl, ten_xb, so_ban)
        self.so_ph = so_ph
        self.thang_ph = thang_ph

    def __str__(self):
        return super().__str__() + ', So phat hanh:%d, Thang phat hanh:%d' % (self.so_ph, self.thang_ph)


class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_xb='', so_ban=0, ngay_ph=0):
        super().__init__(TypeOfDoc.BAO.value, ma_tl, ten_xb, so_ban)
        self.ngay_ph = ngay_ph

    def __str__(self):
        return super().__str__() + ', Ngay phat hanh:%d' % (self.ngay_ph)


class QLTaiLieu:
    def __init__(self):
        self.ds_tai_lieu = []
        self.__data_path_file = 'data.json'

    def input_data(self):
        bl_next = 1
        while bl_next == 1:
            loai = int(input('Loại tài liệu(0:Sách/1:Tạp chí/2:Báo): '))
            ma_tl = str(input('Mã tài liêu: '))
            ten_xb = str(input('Tên xuất bản: '))
            so_ban = int(input('Số bản phát hành: '))
            if loai == 0:  # Sách
                ten_tg = str(input('Ten tac gia: '))
                so_trang = int(input('Số trang: '))
                self.ds_tai_lieu.append(Sach(ma_tl, ten_xb, so_ban, ten_tg, so_trang))
                self.save_data()
            elif loai == 1:  # Tạp chí
                so_ph = int(input('Số phát hành: '))
                thang_ph = int(input('Tháng phát hành: '))
                self.ds_tai_lieu.append(TapChi(ma_tl, ten_xb, so_ban, so_ph, thang_ph))
                self.save_data()
            elif loai == 2:  # Báo
                ngay_ph = int(input('Ngày phát hành: '))
                self.ds_tai_lieu.append(Bao(ma_tl, ten_xb, so_ban, ngay_ph))
                self.save_data()
            bl_next = int(input('Nhập "1" để tiếp tục nhập dữ liệu > '))

    def load_data(self):
        docs = read2(self.__data_path_file)
        for doc in docs:
            if doc['doc_type'] == TypeOfDoc.SACH.value:
                self.ds_tai_lieu.append(
                    Sach(doc['ma_tl'], doc['ten_xb'], doc['so_ban'], doc['ten_tg'], doc['so_trang']))
            elif doc['doc_type'] == TypeOfDoc.TAP_CHI.value:
                self.ds_tai_lieu.append(
                    TapChi(doc['ma_tl'], doc['ten_xb'], doc['so_ban'], doc['so_ph'], doc['thang_ph']))
            else:
                self.ds_tai_lieu.append(Bao(doc['ma_tl'], doc['ten_xb'], doc['so_ban'], doc['ngay_ph']))

    def save_data(self):
        write2(self.__data_path_file, list(map(lambda doc: doc.__dict__, self.ds_tai_lieu)))

    def export_excel(self, excel_path_file):
        # Sách
        book_rows = [['Mã tài liệu', 'Nhà xuất bản', 'Số bản', 'Tên tác giả', 'Số trang']]
        for item in self.__find_by_type(TypeOfDoc.SACH):
            book_rows.append([item.ma_tl, item.ten_xb, item.so_ban, item.ten_tg, item.so_trang])

        # Tạp chí
        journal_rows = [['Mã tài liệu', 'Nhà xuất bản', 'Số bản', 'Số phát hành', 'Tháng phát hành']]
        for item in self.__find_by_type(TypeOfDoc.TAP_CHI):
            journal_rows.append([item.ma_tl, item.ten_xb, item.so_ban, item.so_ph, item.thang_ph])

        # Báo
        newsp_rows = [['Mã tài liệu', 'Nhà xuất bản', 'Số bản', 'Ngày phát hành']]
        for item in self.__find_by_type(TypeOfDoc.BAO):
            newsp_rows.append([item.ma_tl, item.ten_xb, item.so_ban, item.ngay_ph])

        # Sheets:
        sheets = ['Sach', 'TapChi', 'Bao']
        data_rows = [book_rows, journal_rows, newsp_rows]
        export_to_excel(excel_path_file, sheets, data_rows)

    def display(self):
        for item in list(self.ds_tai_lieu):
            print(item)

    def search(self, doc_type=TypeOfDoc.SACH):
        for item in self.__find_by_type(doc_type):
            print(item)

    def __find_by_type(self, doc_type=TypeOfDoc.SACH):
        return list(filter(lambda tl: tl.doc_type == doc_type.value, self.ds_tai_lieu))


# MAIN:
qltl = QLTaiLieu()
qltl.load_data()
bl_next = 1
str_excel_file_path_export = 'my_output.xlsx'

while bl_next != 0:
    int_menu = 1
    print('========== BAI TAP 3 ==========')
    print('1: Hiển thị tất cả tài liệu')
    print('2: Nhập dữ liệu')
    print('3: Tìm kiếm theo loại tài liệu')
    print('4: Xuất ra file Excel')
    int_menu = int(input('Lua chon menu > '))

    if int_menu == 1:
        print('------ DANH SACH TAI LIEU ------')
        qltl.display()
    elif int_menu == 2:
        print('------ NHAP DU LIEU ------')
        qltl.input_data()
    elif int_menu == 3:
        int_type_of_doc = 1
        print('------ TIM KIEM THEO LOAI TAI LIEU ------')
        print('1: Sách')
        print('2: Tạp chí')
        print('3: Báo')
        int_type_of_doc = int(input('Tim kiem theo loai tài liệu > '))
        if int_type_of_doc == 1:
            qltl.search(TypeOfDoc.SACH)
        elif int_type_of_doc == 2:
            qltl.search(TypeOfDoc.TAP_CHI)
        elif int_type_of_doc == 3:
            qltl.search(TypeOfDoc.BAO)
    elif int_menu == 4:
        print('Bắt đầu export file:', str_excel_file_path_export)
        qltl.export_excel(str_excel_file_path_export)
        print('Kết thúc export file:', str_excel_file_path_export)

    bl_next = int(input('Nhập "0" để thoát chương trình > '))
