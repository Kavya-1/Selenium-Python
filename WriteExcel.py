import openpyxl

path = "E:\\edureka\\Assignment9\\testdata\\demo.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet1"]
for r in range(1, 4):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "Welcome"
workbook.save(path)
workbook.close()
