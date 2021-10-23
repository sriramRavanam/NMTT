### python script to change the old names to the official district names.
import glob
import openpyxl as op

officialNameFile = "./result/NamesToChange"

# lines = []
with open(officialNameFile,"r") as file:
    lines = file.readlines()

lines = list(map(lambda x: x.strip() , lines))

dictValues = {}

for s in lines:
    split = s.split(" - ")
    value = split[-1]
    key = "".join(split[:-1])

    dictValues[key] = value


# excelFilesPath = "test2"
excelFilesPath = "mathTransformed"
typeOfFile = "*.xlsx"

excelFilesList = glob.glob(excelFilesPath+"/"+typeOfFile)

for excel in excelFilesList:
    # we take the path to excel files

    wb = op.load_workbook(excel)
    ws = wb.worksheets[0]

    maxRows = ws.max_row + 1
    
    for rowIdx in range(3,maxRows):
        district = ws.cell(row = rowIdx, column = 7).value
        
        if district in dictValues:
            ws.cell(row = rowIdx, column= 7).value = dictValues[district]

    wb.save(excel)



