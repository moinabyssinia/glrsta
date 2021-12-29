
"""  
Created on Thu Dec 16 16:47:00 2021

concatenate all pixel grid data column wise 

@author: Michael Getachew Tadesse

"""
import glob
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\GLRSTA\\data"\
                                "\\Climate\\pixel_variables\\concatenated\\ret"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\GLRSTA\\data\\"\
                                "Climate\\pixel_variables\\pixel_concat_columnwise"
                
                
os.chdir(home_dir)
                
# merging the files
joined_files = os.path.join(home_dir, "*.csv")

# a list of all joined files is returned
joined_list = glob.glob(joined_files)

# to set 'date' as index
indexer = lambda x: pd.read_csv(x)[['date', 'ret']].set_index('date')

# files are joined
df = pd.concat(map(indexer, joined_list), join = "inner", axis = 1, ignore_index = True)


os.chdir(out_dir)
df.to_csv("all_Pixels_ret.csv")
print(df)