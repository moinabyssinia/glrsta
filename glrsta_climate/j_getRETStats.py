
"""  
Created on Thu Dec 16 17:05:00 2021

get statistics for the RET (about 4818 pixels) 

@author: Michael Getachew Tadesse

"""
import glob
import os 
import pandas as pd 


home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\GLRSTA\\data\\"\
                                "Climate\\pixel_variables\\pixel_concat_columnwise"
                
                
os.chdir(home_dir)
                

dat = pd.read_csv("all_Pixels_ret.csv")
print(dat)

dat['mean'] = dat.iloc[:,1:].mean(axis = 1)
print(dat)

dat[['date', 'mean']].to_csv("mean_RET.csv")