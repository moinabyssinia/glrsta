"""  
Created on Thu Sep 23 16:13:00 2021
modified on Wed Oct 06 18:03:00 2021
modified on Mon Nov 01 14:13:00 2021
modified on Wed Nov 24 14:20:00 2021

prepare dfs0 withdrawal files with the 
units, types and datatypes included - but for pumping rate

@author: Michael Getachew Tadesse

"""

import os
from datetime import datetime
from mikecore.DfsFile import DataValueType
from mikeio import Dfs0, Dataset
from mikeio.eum import ItemInfo, EUMType, EUMUnit
import pandas as pd 
from mikeio import Dfs0

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables\\concatenated\\ret"

dirOut = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables\\dfs0\\ret"


os.chdir(dirHome)


# loop through pixels
pixels = os.listdir()

for px in pixels:
    os.chdir(dirHome)

    print(px)

    dat = pd.read_csv(px)[['date', 'ret']]
        

    df = []
    items = []
    for ii in range(1,dat.shape[1]):
        df.append(dat.iloc[:,ii].to_numpy())

        items.append(ItemInfo(dat.columns[ii], EUMType.Evapotranspiration_Rate, 
                                EUMUnit.mm_per_day, 
                                    data_value_type= DataValueType.MeanStepBackward))

    # generate daily time from 01/2000 to 12/2017 - B, D: day freq
    datTime = pd.date_range(start='01/01/2000', end='12/31/2017', freq='D')  
        
    
    '''  
    # writing dataframe to dfs0
    # use meanstepBackward which is same as mean step accumulated

    '''
    ds = Dataset(data = df, time = datTime, items = items)
    print(ds)


    # write the dfs0 file
    
    os.chdir(dirOut)
    
    dfs = Dfs0()

    dfs.write(filename= px.split(".csv")[0] + ".dfs0", 
            data=ds,
            title="Reference Evapotranspiration (ETo)")