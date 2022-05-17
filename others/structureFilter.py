"""
Created on Thu May 4 15:25:34 2022

To filter structure information based
on different models

0 : weir
1 : culvert
2 : pump
3 : control structures

*change end section indication part manually

@author: Michael Getachew Tadesse

"""

import os 
import logging
import pandas as pd

# select structure type

str_type = "ctrl_stru"

struct = {"weirs" : "0",
          "culverts" : "1",
          "pumps" : "2",
          "ctrl_stru" : "3"
          }


# define model file locations 
weirs = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BCB\\data\\weirs"
culverts = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BCB\\data\\culverts"
pumps = ""
bridges = ""
ctrl_stru = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BCB\\data\\ctrl_stru"


# read list of filtered out struture names
dat = pd.read_csv("structures.csv")
# dat = pd.read_csv("test_structures.csv")




print(int(struct[str_type])/1.0)
dat = dat[dat['Str_Type'] == int(struct[str_type])/1.0]
dat.reset_index(inplace = True)
print(dat)


# define model file names
modelName = {
    "BCB_C1" : "bcb.txt",
    "CCWHP" : "cc.txt",
    "SLWCI" : "slcwi.txt"
}

##############################################
# change the saving file name
##############################################

# start logging
logging.basicConfig(filename= str_type + ".log", encoding='utf-8', level=logging.DEBUG)

with open("bcbUpdated" + str_type + ".txt", "w") as f:

    # select structure type
    os.chdir(str_type)
    
    for ii in range(len(dat)):
        id = dat['Str_ID'][ii]
        branch = dat['Str_BrName'][ii]
        # chainage = dat['Str_Ch'][ii].astype(str).split(".0")[0]
        chainage = dat['Str_Ch'][ii]
        model = dat['Model'][ii]
        
    
        # print("Location = {}, {}, {}".format(id, chainage, model))
    
        infile = open(modelName[model], 'r').readlines()

        prev_line = ""
        copyLines = False
        
        for line in infile:
            # print(line)

            # just for control structures - following selection
            if ("Location = '{}', {}, '{}'".format(branch, chainage, id) in line) | \
                ("Location = '{}', {}, '{}'"
                    .format(branch, chainage.astype(str).split(".0")[0], id) in line): 
                # print(line)
                f.write(prev_line)
                # f.write("\n")
                copyLines = True
                
                logging.info(id)
            
            if copyLines:
                ######################################
                # change end line string
                ######################################
                if "EndSect  // control_str_data" in line:
                    f.write(line)
                    # f.write("\n")
                    break
                else: 
                    f.write(line)
                    # f.write("\n")
            
            
            prev_line = line
    