from quanlytailieu import QLTaiLieu

# Config:
db_name = 'my_db'

# Main:
qltl = QLTaiLieu(db_name)
bl_next = 1

while bl_next != 0:
    int_menu = 1
    print('========== BAI TAP QUAN LY THU VIEN ==========')
    print('1: Hiển thị thông tin tài liệu')
    print('2: Tìm kiếm tài liệu')
    print('3: Thêm tài liệu (nhập tay)')
    print('4: Thêm tài liệu (tự động từ "data.json")')
    print('5: Sửa tài liệu')
    print('6: Xoá tài liệu')
    print('Khác: Thoát\n')
    if not qltl.check_data_exists():
        print('!!!Không tìm thấy data "%s" trong CSDL. Chọn menu 3 hoặc 4 để tạo dữ liệu trước!!!' % (db_name))
    int_menu = int(input('Lựa chọn menu > '))

    if int_menu == 1:
        qltl.display()
    elif int_menu == 2:
        qltl.search()
    elif int_menu == 3:
        qltl.input_data()
    elif int_menu == 4:
        qltl.input_data_auto()
    elif int_menu == 5:
        qltl.update()
    elif int_menu == 6:
        qltl.delete()
    else:
        break
    print('==============================================')
    bl_next = int(input('Nhập "0" để thoát chương trình > '))
