
"""  
Created on Fri Nov 26 15:45:00 2021

concatenate all pixel grid data column wise 

@author: Michael Getachew Tadesse

"""
import re
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\GLRSTA\\data"\
                                "\\Climate\\pixel_variables\\concatenated\\ret"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\GLRSTA\\data\\"\
                                "Climate\\pixel_variables\\pixel_concat_columnwise"
                
os.chdir(home_dir)

files = os.listdir()

isFirst = True
for file in files:
    print(file)
    
    if isFirst:
        dat = pd.read_csv(file)[['date', 'ret']]
        
        colName = file.split('.csv')[0]
        dat.columns = ['date', colName]
        
        df = dat
        isFirst = False
    else:
        dat = pd.read_csv(file)[['date', 'ret']]
        
        colName = file.split('.csv')[0]
        dat.columns = ['date', colName]
        
        df = pd.concat([df, dat])

        
os.chdir(out_dir)
df.to_csv("all_Pixels_ret.csv")