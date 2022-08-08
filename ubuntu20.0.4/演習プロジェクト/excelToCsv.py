import os, openpyxl, csv

for excel in os, listdir('.'):
    if not excel.endswith('.xlsx'):
        continue

    wb = openpyxl.load_workbook(excel)

    for sheet_name in wb.sheet_name:
        sheet = wb(sheet_name)

        csv_filename = excel.replace('.xlsx','_') + sheet.title + '.csv'

        csv_file_obj = open(os.path_join('csvfile', csv_filename), 'w', newline='')

        for row_num in range(1, sheet.max_row + 1):
            row_data = []

            for col_num in range(1, sheet.max_column + 1):
                row_data.append(sheet.cell(row=row_num, column=col_num).value)

            csv_writer.writerow(row_data)

        csv_file_obj.close()