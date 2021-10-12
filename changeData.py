import os
import openpyxl as op


dir = "test"

excelFiles = os.listdir(dir+"\.")

for file in excelFiles:
    filePath = dir+"/"+file
    wb = op.load_workbook(filename=filePath)
    ws = wb.active

    val = ws["B3"].value
    val = val.split("\n") #\n separates the name and the address
    name,address = val 
    schoolName,town,district = address.split(", ")  # 
    district = district[:-1]    #everything except last character because '.' is present at the end.

    # the 3rd column typically has NAME\nADDRESS.
    # 
    # address has schoolName,town,district

    print(schoolName,district,name,town)

    # for row in ws.iter_rows(min_row=2,values_only=True):
    #     for value in row:
    #         print(value)