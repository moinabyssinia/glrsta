
"""  
Created on Tue Dec 28 13:33:00 2021

Find similarities between strings

@author: Michael Tadesse

"""

import difflib
import os 
import pandas as pd

os.chdir("C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\GLRSTA\\"\
            "gis\\UZ\\simplified_gridcodes")

# print(os.listdir())

dat_main = pd.read_csv("main.csv", header = None)
dat_soils = pd.read_csv("fl127.csv")

# print(dat_soils['muname'][46])
print(dat_main[0])

# print(difflib.SequenceMatcher(None, dat_soils['muname'][46], dat_main[0][27]).ratio())

compareSimilarity = lambda x, y: difflib.SequenceMatcher(
                        None, x, y).ratio()



dat_soils['soil_num'] = 'nan'
dat_soils['soil_name'] = 'nan'

for ii in range(len(dat_soils)):
    print(ii)
    comp_result = pd.DataFrame(list(map(compareSimilarity, 
                        dat_soils['muname'][ii], dat_main[0])))
    ind = comp_result[0].idxmax()
    
    soil_name = dat_main[0][ind]
    
    dat_soils['soil_num'][ii] = ind
    dat_soils['soil_name'][ii] = soil_name


dat_soils[['muname', 'soil_num', 'soil_name']].to_csv('simplified_grid_codes.csv')