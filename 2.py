import tkinter as tk
from tkinter import filedialog, Text
import os
import openpyxl
import pandas as pd

from openpyxl.utils.dataframe import dataframe_to_rows
from cs50 import get_string
from cs50 import get_int


import glob

fileList = glob.glob(r'\\172.23.102.26\Users\User\Downloads\*(?).xlsx', recursive=True)
for file in fileList:
    try:
        os.remove(file)
    except OSError:
        print("Error while deleting file")


root = tk.Tk()
apps = []




def erase_space(raw_str): 
    str_to_list = raw_str.split(' ')

    new_list = []
    def erase_space(variable): 
        if variable != '': 
            return True
        else: 
            return False

    filtered = filter(erase_space, str_to_list) 

    for s in filtered: 
        new_list.append(s)

    str1 = ""      
    for ele in new_list:  
        str1 += ele  
    return str1     

def addapp():

    

    filename = filedialog.askopenfilename(
        initialdir='C:/Users/user/Documents', multiple=True, title="Select file", filetypes=(("excel", "*.xlsx"), ("all files", "*.*")))
    for widget in frame.winfo_children():
        widget.destroy()
    list_file = list(filename)
    for file in list_file:
            apps.append(file)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white", borderwidth=2, relief="groove")
        label.pack()


def runapps():
    result = None
    for app in apps:
        wb = openpyxl.load_workbook(app)
        wb.active = 1
        ws = wb.active

        df = pd.DataFrame(ws.values)
        new_pivot = pd.pivot_table(df, values=[4], columns=[2], aggfunc='sum')

        new_list = new_pivot.to_dict(orient='list')
        brand_new_df = pd.DataFrame(new_list)


        stringx = app
        urutanbs = stringx.index("/",34,37)
        x = (len(stringx) - urutanbs - 1) * -1
        app = stringx[x:]
        app = erase_space(app)
        t = app.rfind('.',20)
        app = app[:t]
        
        file_name = [app] 
        print(file_name)
        brand_new_df['app'] = file_name


        frames = [result, brand_new_df]
        result = pd.concat(frames)

   
    
    
    
    dummy_dict = {'app': ['Null.xlsx'],
                  'BPM Number': ['OPDD'],
                  4851044:[0],
                  4851005:[0],
                  4851033:[0],
                  4851278:[0],
                  4851282:[0]
                  }
                  
    dummy_df = pd.DataFrame(dummy_dict, columns = [4851044,4851005,4851033,4851278,4851282,'app','BPM Number'])
    
    frames = [result, dummy_df]
    result = pd.concat(frames)
    
    
    newDF = result[[4851044,4851005,4851033,4851282,4851278,'app']]

    cars = {'app': ['Shopee1.xlsx','Shopee2.xlsx'],
            'BPM Number': [22000,25000]
            }

    df2 = pd.DataFrame(cars, columns = ['app', 'BPM Number'])

    
    xxx = pd.read_excel(r'\\172.23.102.26\Users\User\Downloads\BPMtoExcel.xlsx', index_col=0)
    
    
    
    Outer_join = pd.merge(xxx, newDF, on ='app', how ='outer') 
    Outer_join = Outer_join[[4851044,4851005,4851033,4851282,4851278,'BPM Number','app']]
    Outer_join.to_excel(r'\\172.23.102.26\Users\User\Downloads\OuterJoin.xlsx')
    os.startfile(r'\\172.23.102.26\Users\User\Downloads\OuterJoin.xlsx')

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openapp = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addapp)
openapp.pack()

runapps = tk.Button(root, text="Process Summary", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runapps)
runapps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
