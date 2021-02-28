import os
import glob
fileList = glob.glob(r'C:\Users\user\Documents\Abi\delete\*(*).accdb', recursive=True)
for file in fileList:
    try:
        os.remove(filePath)
    except OSError:
        print("Error while deleting file")
