
"""  
Created on Tue Dec 28 13:33:00 2021

This program finds the similarity between the soil types 
from the nine counties to the 40 soil types from the 
SFWMDFPLOS soil database 

@author: Michael Tadesse

"""

import os 
import math 
import re 
import pandas as pd
from cosine import get_result

os.chdir("C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\GLRSTA\\"\
            "gis\\UZ\\simplified_gridcodes")

# get data 
dat_main = pd.read_csv("main.csv", header = None)
dat_soils = pd.read_csv("allSoilData_nine_counties.csv")


dat_soils['soil_num'] = 'nan'
dat_soils['soil_name'] = 'nan'


# for ii in range(len(dat_soils)):
for ii in range(len(dat_soils)):
    print(ii, "-", dat_soils['muname'][ii])
    
    result = []
    
    for jj in range(len(dat_main)):
        comp_result = get_result(dat_soils['muname'][ii], dat_main[0][jj])
        result.append(comp_result)
    
    result = pd.DataFrame(result)
    ind = result[0].idxmax()
    
    
    soil_name = dat_main[0][ind]
    
    
    dat_soils['soil_num'][ii] = ind
    dat_soils['soil_name'][ii] = soil_name


dat_soils.to_csv('allSoilData_nine_counties_consolidated.csv')