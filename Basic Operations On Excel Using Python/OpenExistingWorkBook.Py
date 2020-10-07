import openpyxl

wb = openpyxl.load_workbook("Our First Workbook.xlsx")
for sheet in wb:
    print(sheet.title)
