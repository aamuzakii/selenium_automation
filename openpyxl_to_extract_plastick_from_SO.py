import openpyxl
import os
import pandas as pd

from openpyxl.utils.dataframe import dataframe_to_rows
from cs50 import get_string
from cs50 import get_int


os.chdir(r'C:\Users\user\Documents')

file_number = get_int("How many: ")

Files = []
result = None

for x in range(file_number):
    file__name = get_string("File Name: ") + ".xlsx"
    Files.append(file__name)
    print(Files)

for File in Files:
    wb = openpyxl.load_workbook(File)
    ws = wb['Sheet1']

    df = pd.DataFrame(ws.values)
    new_pivot = pd.pivot_table(df, values=[4], columns=[2], aggfunc='sum') 
    frames = [result, new_pivot]
    result = pd.concat(frames)
    print(result)
