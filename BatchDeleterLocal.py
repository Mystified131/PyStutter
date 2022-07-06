#This code imports the necessary modules

import os
import re
import collections
import operator
from subprocess import call
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")) and ('AtmosOut' not in str(filepath)) and ('VoxOut' not in str(filepath)) and ('SoundsOut' not in str(filepath)):
            os. remove(filepath) 

print("")

print("The designated files have been removed. Thank you.")

print("")

print("The sound preparation process has ended.")

print("")

print("Please check the subfolders for your output files.")

print("")

#call(["python", "C:\\Users\\mysti\\Coding\\Pystutter\\DJEthHouse.py"])

## THE GHOST OF THE SHADOW ##