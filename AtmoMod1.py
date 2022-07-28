#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

srchstr = 'H:\\Acid_Loops'

contentdrones = []

contentpepper = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
        
        if  filepath.endswith(".wav") and  (("Drone" in filepath)  or (("Strings" in filepath) ) or (("Pad" in filepath) ) and ("Eth" in filepath)) :  
        #if  filepath.endswith(".wav") and (("Chant" in filepath) or  ("HomeLoops2022" in filepath)) and  (("Pad"in filepath) or ("Strings" in filepath)):  
                         
            contentpepper.append(filepath)

            contentdrones.append(filepath)

print("")

print("Gathering Root Sounds.")

x = len(contentdrones)

for ctr in range(120):
    y = random_number(x)
    atrack = contentdrones[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Pystutter\\newsounddrone' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentdrones[y], outstr)


x = len(contentpepper)

for ctr in range(150):
    y = random_number(x)
    atrack = contentpepper[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Pystutter\\newsoundpepper' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentpepper[y], outstr)


call(["python", "DJProcessorNuAmb.py"])


## THE GHOST OF THE SHADOW ##


