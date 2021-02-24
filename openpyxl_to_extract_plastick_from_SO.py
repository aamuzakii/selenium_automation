import tkinter as tk
from tkinter import filedialog, Text
import os
import openpyxl
import pandas as pd

from openpyxl.utils.dataframe import dataframe_to_rows
from cs50 import get_string
from cs50 import get_int


root = tk.Tk()
apps = []

# if os.path.isfile('save.txt'):
#     with open('save.txt', 'r') as f:
#         tempapps = f.read()
#         tempapps = tempapps.split(',')
#         apps = [x for x in tempapps if x.strip()]
#         print(apps)


def addapp():

    

    filename = filedialog.askopenfilename(
        initialdir='C:/Users/user/Documents', multiple=True, title="Select file", filetypes=(("excel", "*.xlsx"), ("all files", "*.*")))
    for widget in frame.winfo_children():
        widget.destroy()
    # print(type(filename))
    # print(filename)
    list_file = list(filename)
    for file in list_file:
            apps.append(file)
    # print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white", borderwidth=2, relief="groove")
        label.pack()


def runapps():
    result = None
    os.chdir(r'C:\Users\user\Documents')
    print(apps)
    for app in apps:
        wb = openpyxl.load_workbook(app)
        ws = wb['Sheet1']

        df = pd.DataFrame(ws.values)
        new_pivot = pd.pivot_table(df, values=[4], columns=[2], aggfunc='sum')
        print(new_pivot)
        print(" ")

        new_list = new_pivot.to_dict(orient='list')
        print(new_list)
        print(" ")
        brand_new_df = pd.DataFrame(new_list)
        print(brand_new_df)
        print(" ")

        file_name = [app] 
        brand_new_df['app'] = file_name


        frames = [result, brand_new_df]
        result = pd.concat(frames)

    # result_dict = result.to_dict(orient='list')

    # filtered_dict = {}
    # for (key, value) in result_dict.items():
    #     if key == 4851044 or key == 4851005 or key == 4851033 or key == 'app':
    #         filtered_dict[key] = value

    # newDF = pd.DataFrame(filtered_dict)
    # print(newDF)
    newDF = result[[4851044,4851005,4851033,'app']]

    cars = {'app': ['Shopee1.xlsx','Shopee2.xlsx'],
            'BPM Number': [22000,25000]
            }

    df2 = pd.DataFrame(cars, columns = ['app', 'BPM Number'])

    print(df2)

    
    Outer_join = pd.merge(newDF, df2, on ='app', how ='outer') 
    Outer_join.to_excel(r'C:\Users\user\Documents\OuterJoin.xlsx')
    os.startfile(r'C:\Users\user\Documents\OuterJoin.xlsx')


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openapp = tk.Button(root, text="Open app", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addapp)
openapp.pack()

runapps = tk.Button(root, text="Make Summary", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runapps)
runapps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
