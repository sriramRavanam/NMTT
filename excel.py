import openpyxl as opxl
import urllib.request as req 

def convertToCode(str):
    res = ""
    for i in str.split():
        res+=i[0]

    sorted_list = sorted(res)

    return "".join(sorted_list)

numEntries = 200
pathToExcel = "raw_table_data.xlsx"

wb = opxl.load_workbook(pathToExcel)
sheet = wb.active

#cell column relative name
natureOfProgram = 'A'
title = 'B'
numDays = 'C'
duration = 'D'
numParticipants = 'E'
numResourcePersons = 'F'
URL = 'G'
resultsLink = 'H'

#durationFrom = "From 02-02-2021"
#durationFrom[5:] = "02-02-2021"

#durationTo = "To 02-02-2021"
#durationTo[3:] = "02-02-2021"

#sheet[i] is a tuple

codes = []
code = {}

pathToFolder = "./test2/"
# maxRow = numEntries+1
maxRow = 20
for i in range(1,maxRow):
    rowNum_1 = 2*i
    rowNum_2 = 2*i+1

    (natureOfProgramCell,titleCell,numDaysCell,durationFromCell,numParticipantsCell,numResourcePersonsCell,urlCell,resultsLinkCell) = sheet[rowNum_1]
    (_,_,_,durationToCell,_,_,_,_) = sheet[rowNum_2]

    #get data from link
    titleCode = convertToCode(titleCell.value)    
    fromDate = durationFromCell.value
    toDate = durationToCell.value
    fileName = titleCode+"_("+fromDate[5:7]+"-"+toDate[3:5]+")"+toDate[5:]+"_"+str(numParticipantsCell.value)+"_"+str(numResourcePersonsCell.value)+".pdf"
    
    # #resultsLinkCell - type - MergedCell
    if resultsLinkCell is not None:
        link = resultsLinkCell.value

        if titleCode not in codes:
            codes.append(titleCode)
            code[titleCode] = titleCell.value

        req.urlretrieve(link,pathToFolder+fileName)


legendName = "legend.txt"
with open(pathToFolder+legendName,"w") as file:
    for id in codes:
        line = str(id)+" : "+str(code[id])+"\n"
        file.write(line)
    
file.close()


# (natureOfProgramCell,titleCell,numDaysCell,durationFromCell,numParticipantsCell,numResourcePersonsCell,urlCell,resultsLinkCell) = sheet[2]
# (_,_,_,durationToCell,_,_,_,l) = sheet[3]


#get data from link
# import urllib.request
# urllib.request.urlretrieve(url, "filename.pdf")
# titleCode = convertToCode(titleCell.value)    
# fromDate = durationFromCell.value
# toDate = durationToCell.value
# fileName = titleCode+"_("+fromDate[5:7]+"-"+toDate[3:5]+")"+toDate[5:]+"_"+str(numParticipantsCell.value)+"_"+str(numResourcePersonsCell.value)
# filePath = r".\test\\"+fileName


# #resultsLinkCell - type - MergedCell
# link = resultsLinkCell.value

# # #url retrieve works.
# req.urlretrieve(link,f"./test/{fileName}.pdf")

#duration
# durationCell = duration + str(2)
# x = sheet[durationCell].value
# print(x[5:])
# for i in l:
#     print(i.value,end= " | ")
