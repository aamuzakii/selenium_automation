# Python Openpyexcel Cheatsheet

import openpyxl

openpyxl.__version__
'3.0.5'

import os

os.chdir(r'C:\Users\user\Documents')

wb = openpyxl.load_workbook('ABC.xlsx')


sheet = wb['Sheet1']
print(sheet)
sheet['A1'].value

ws = wb.active
for row in ws.rows:
    if(row[0].value == "OPDDFH-02"):
        opddfh = row[0]
        msa = opddfh.offset(0,1).value
        print(msa)
