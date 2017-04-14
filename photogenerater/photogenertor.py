import os
import xlwt
from os import listdir

fileList = listdir("/Users/allenzhu/Desktop/test")
newList = []
#print fileList
wb = xlwt.Workbook()
ws = wb.add_sheet('photos')
count = 0
ws.write(count,count,'targetid')
ws.write(count,count+1,'dirname')
for index in range(len(fileList)):
    namesep = fileList[index].split('.')
    newList.append(namesep[0])
print newList

for photo in range(len(newList)):
    filename = '/Users/allenzhu/Desktop/photogenerator/' + newList[photo] + '.jpg'
    ws.write(photo+1,0,newList[photo])
    ws.write(photo+1,1,filename)
wb.save('result.xls')