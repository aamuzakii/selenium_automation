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

df.loc[2,2]
# result: 5655037

pivot
# result
#                                4
# 2
# 4851033                       18
# 4851044                       18
# 5469891                       13
# 5654125                        1
# 5655037                        1
# 5655149                        2
# 5655451                        1
# 5655646                        2
# 5656099                        1
# 5656317                        7
# 5656318                        3


pivot[4]
# 2
# 4851033                         18
# 4851044                         18
# 5469891                         13
# 5654125                          1
# 5655037                          1
# 5655149                          2
# 5655451                          1
# 5655646                          2
# 5656099                          1
# 5656317                          7
# 5656318                          3


