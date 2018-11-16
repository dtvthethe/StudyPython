from openpyxl import Workbook


def export_to_excel(excel_file_path, sheet_names, data_rows):
    wb = None
    try:
        wb = Workbook()
        for i in range(0, len(sheet_names)):
            ws = wb.create_sheet(title=sheet_names[i])
            for row in data_rows[i]:
                ws.append(row)
        wb.save(excel_file_path)
    except BaseException as be:
        print(be)
    finally:
        if wb is not None: wb.close()
