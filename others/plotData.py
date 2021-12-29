"""
Created on Wed Dec 22 14:37:00 2021

plotting script

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
            "MIKE_Modeling_Group - Documents\\GLRSTA\\models\\"\
                    "MIKE_SHE_Hydro\\MSHE\\GLRSTA_case3.she - Result Files\\"\
                            "water_budget"

os.chdir(dirHome)


def plotIt(variable):
    '''  '''
    dat = pd.read_csv("case3_incremental_wbl.csv")
    dat['Date'] = pd.to_datetime(dat['Date'])

    print(dat.columns)


    plt.figure(figsize = (16,5))
    plt.plot(dat['Date'],  dat[variable])
    
    plt.title(variable)

    plt.legend()
    plt.show()

    print(dat)
    


def plotAll():
    dat = pd.read_csv("case3_incremental_wbl.csv")
    dat['Date'] = pd.to_datetime(dat['Date'])

    print(dat.columns)
    
    dat.melt('Date', var_name = 'cols', value_name = 'vals')
    
    g = sns.lineplot(x = 'Date', y = 'vals', hue = 'cols', data = dat)
    
    plt.show()
    
    
plotAll()
