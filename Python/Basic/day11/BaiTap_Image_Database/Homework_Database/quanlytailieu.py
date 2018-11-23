from enum import Enum
from doc import Sach, TapChi, Bao
from mongodb_utility import MongoUtility
import json_utility


class TypeOfDoc(Enum):
    SACH = 1
    TAP_CHI = 2
    BAO = 3


class QLTaiLieu:
    def __init__(self, db_name, host='localhost', port=27017, collection_book_name='book',
                 collection_newspaper_name='newspaper', collection_journal_name='journal'):
        self.__db = MongoUtility(host, port, db_name)
        self.__collection_book_name = collection_book_name
        self.__collection_newspaper_name = collection_newspaper_name
        self.__collection_journal_name = collection_journal_name
        self.__data_path_file = 'data.json'

    def check_data_exists(self):
        return True if len(self.__db.connect().list_collection_names()) > 0 else False

    def input_data(self):
        bl_next = 1
        while bl_next == 1:
            table_name = self.__select_table()
            if table_name is not None:
                ma_tl = str(input('Mã tài liêu: '))
                ten_xb = str(input('Tên xuất bản: '))
                so_ban = int(input('Số bản phát hành: '))
                if table_name == self.__collection_book_name:  # Sách
                    ten_tg = str(input('Ten tac gia: '))
                    so_trang = int(input('Số trang: '))
                    id_inserted = self.__db.insert_entry(self.__collection_book_name,
                                                         Sach(ma_tl, ten_xb, so_ban, ten_tg, so_trang).__dict__)
                elif table_name == self.__collection_journal_name:  # Tạp chí
                    so_ph = int(input('Số phát hành: '))
                    thang_ph = int(input('Tháng phát hành: '))
                    id_inserted = self.__db.insert_entry(self.__collection_journal_name,
                                                         TapChi(ma_tl, ten_xb, so_ban, so_ph, thang_ph).__dict__)
                elif table_name == self.__collection_newspaper_name:  # Báo
                    ngay_ph = int(input('Ngày phát hành: '))
                    id_inserted = self.__db.insert_entry(self.__collection_newspaper_name,
                                                         Bao(ma_tl, ten_xb, so_ban, ngay_ph).__dict__)
                print('Thêm thành công dữ liệu ID = %s' % (id_inserted))
                bl_next = int(input('Nhập "1" để tiếp tục nhập dữ liệu > '))

    def input_data_auto(self):
        print('Bắt đầu nhập dữ liệu')
        docs = json_utility.read(self.__data_path_file)
        for doc in docs:
            if doc['doc_type'] == TypeOfDoc.SACH.value:
                id_inserted = self.__db.insert_entry(self.__collection_book_name,
                                                     Sach(doc['ma_tl'], doc['ten_xb'], doc['so_ban'], doc['ten_tg'],
                                                          doc['so_trang']).__dict__)
            elif doc['doc_type'] == TypeOfDoc.TAP_CHI.value:
                id_inserted = self.__db.insert_entry(self.__collection_journal_name,
                                                     TapChi(doc['ma_tl'], doc['ten_xb'], doc['so_ban'], doc['so_ph'],
                                                            doc['thang_ph']).__dict__)
            else:
                id_inserted = self.__db.insert_entry(self.__collection_newspaper_name,
                                                     Bao(doc['ma_tl'], doc['ten_xb'], doc['so_ban'],
                                                         doc['ngay_ph']).__dict__)
            print('Thêm thành công dữ liệu ID = %s' % (id_inserted))
        print('Kết thúc nhập dữ liệu')

    def display(self):
        table_name = self.__select_table()
        if table_name is not None:
            print('----- Table: %s -----' % (table_name))
            dt = self.__db.get_all(table_name)
            for item in self.__map_table_to_object(table_name, dt):
                print(item)

    def search(self):
        table_name = self.__select_table()
        if table_name is not None:
            print('----- Search on Table: %s -----' % (table_name))
            int_search_by = int(input('1) Mã tài liệu\n2) Tên nhà xuất bản\nTìm kiếm theo > '))
            if int_search_by == 1:
                str_ma_tl = str(input('Nhập mã tài liệu cần tìm > '))
                dt = self.__db.search(table_name, {'ma_tl': {'$regex': str_ma_tl}})
            elif int_search_by == 2:
                str_ten_xb = str(input('Nhập tên nhà xuất bản cần tìm > '))
                dt = self.__db.search(table_name, {'ten_xb': {'$regex': str_ten_xb}})
            for item in self.__map_table_to_object(table_name, dt):
                print(item)

    def delete(self):
        table_name = self.__select_table()
        if table_name is not None:
            ma_tl = str(input('Mã tài liêu: '))
            deleted = self.__db.delete(table_name, {'ma_tl': ma_tl})
            if deleted > 0:
                print('Xoá thành công %d trường dữ liệu' % (deleted))
            else:
                print('Xoá thất bại')

    def update(self):
        table_name = self.__select_table()
        if table_name is not None:
            str_ma_tl = str(input('Nhập vào mã tài liệu cần update > '))
            if self.__db.search(table_name, {'ma_tl': str_ma_tl}).count() > 0:
                ten_xb = str(input('Tên xuất bản: '))
                so_ban = int(input('Số bản phát hành: '))
                if table_name == self.__collection_newspaper_name:
                    ngay_ph = int(input('Ngày phát hành: '))
                    row_updated = self.__db.update_entry(table_name, {'ma_tl': str_ma_tl},
                                                         {'ten_xb': ten_xb, 'so_ban': so_ban, 'ngay_ph': ngay_ph})
                elif table_name == self.__collection_journal_name:
                    so_ph = int(input('Số phát hành: '))
                    thang_ph = int(input('Tháng phát hành: '))
                    row_updated = self.__db.update_entry(table_name, {'ma_tl': str_ma_tl},
                                                         {'ten_xb': ten_xb, 'so_ban': so_ban, 'so_ph': so_ph,
                                                          'thang_ph': thang_ph})
                elif table_name == self.__collection_book_name:
                    ten_tg = str(input('Ten tac gia: '))
                    so_trang = int(input('Số trang: '))
                    row_updated = self.__db.update_entry(table_name, {'ma_tl': str_ma_tl},
                                                         {'ten_xb': ten_xb, 'so_ban': so_ban, 'ten_tg': ten_tg,
                                                          'so_trang': so_trang})
                if row_updated > 0:
                    print('Update thành công %d trường dữ liệu' % (row_updated))
                else:
                    print('Update không thành công')
            else:
                print('Không tìm thấy dữ liệu nào có mã = "%s"' % (str_ma_tl))

    def __select_table(self):
        print('Lựa chọn bảng cần thao tác:')
        collections = self.__db.get_collections()
        for i in range(0, len(collections)):
            print(i, ') ', collections[i])
        int_table = int(input('bảng > '))
        if int_table not in range(0, len(collections)):
            return None
        return collections[int_table]

    def __map_table_to_object(self, collection_name, data_rows):
        lst_document = []
        if collection_name == self.__collection_book_name:
            for data_row in data_rows:
                lst_document.append(
                    Sach(data_row['ma_tl'], data_row['ten_xb'], data_row['so_ban'], data_row['ten_tg'],
                         data_row['so_trang']))
        elif collection_name == self.__collection_newspaper_name:
            for data_row in data_rows:
                lst_document.append(
                    Bao(data_row['ma_tl'], data_row['ten_xb'], data_row['so_ban'], data_row['ngay_ph']))
        elif collection_name == self.__collection_journal_name:
            for data_row in data_rows:
                lst_document.append(
                    TapChi(data_row['ma_tl'], data_row['ten_xb'], data_row['so_ban'], data_row['so_ph'],
                           data_row['thang_ph']))
        return lst_document
