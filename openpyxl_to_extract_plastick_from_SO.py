# Python Openpyexcel Cheatsheet
# $ pip install openpyxl

import openpyxl
import os
import pandas as pd

from openpyxl.utils.dataframe import dataframe_to_rows



os.chdir(r'C:\Users\vivo\Downloads')

wb = openpyxl.load_workbook('Order 21.02.19  - 1 Shopee (POP) REG.xlsx')

sheet = wb['IDOS002-Shopee 1-10']

# ws = wb.active

df = pd.DataFrame(ws.values)
