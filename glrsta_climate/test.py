
"""  
Created on Fri Nov 19 15:51:00 2021

testing data

@author: Michael Getachew Tadesse

"""
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\clipped2MD"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\other"
        
os.chdir(home_dir)

files = os.listdir()


dat = pd.read_csv("Florida_1985.txt", engine='python')
print(dat.columns)

print(dat)

dat.reset_index(inplace = True)
dat.drop(['Unnamed: 0', 'index'], axis = 1, inplace = True)
    
print(dat.columns)

# the tab delimited files don't have 'albedo' 
dat.columns = ['date', 'lat', 'lon', 'pixel', 'pet', 'ret', 'solar',
                'rhmax', 'rhmin', 'tmax', 'tmin', 'ws', 'isInside']


dat = dat[dat['date'] < 19850102]

print(dat)

os.chdir(out_dir)
dat.to_csv("test1985.csv")
