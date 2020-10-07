from openpyxl import Workbook

if __name__=="__main__":
    filename = "Looping.xlsx"
    wb = Workbook()

    ws1 = wb["Sheet"]
    
    for row in range(1,4):
        for col in range(1,4):
            cell = ws1.cell(row=col,column= row)
            print(cell.coordinate, end="")
        print()

#Save Workbook
wb.save(filename)
