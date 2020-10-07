from openpyxl import load_workbook

wb = load_workbook("added_sheetss.xlsx")

for sheet in wb:
    print(sheet.title)

source = wb["Sheet nr 2"]

new_sheet = wb.copy_worksheet(source)

new_sheet.tile = "Copied Sheet nr 2"

wb.save("copied_sheets.xlsx")
