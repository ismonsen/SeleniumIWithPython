import openpyxl

path = 'data2.xlsx'

wb = openpyxl.load_workbook(path)
sheet = wb['лист 1']

for row in range(1, 8):
    for col in range(1, 8):
        sheet.cell(row=row, column=col).value = f'{row}try{col}'
    print()
wb.save(path)
