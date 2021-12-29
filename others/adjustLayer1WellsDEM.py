"""
Created on Mon Dec 13 17:27:00 2021

To adjust the elevation of layer 1 wells elevation
match the DEM elevation if well elevation > DEM
only for layer 1 wells

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\GLRSTA\\gis\\compare_DEM_wellTop"

os.chdir(dirHome)


dat = pd.read_csv('ecftxwellDEM_analysis.csv')

dat['outlier'] = (dat['layer'] == '1') & (dat['top'] > dat['dem_value1'])
dat['diff'] = dat['top'] - dat['dem_value1']

dat.to_csv('ecftxwellDEM_layer1_adjusted.csv')
