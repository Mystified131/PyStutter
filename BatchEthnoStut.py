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

#srchstr = 'E:\\EthnoSoundSources'

srchstr = 'E:\\Acid_Loops'

ethcont = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
         
        if  filepath.endswith(".wav") and (("Ethno" in filepath) or ("World" in filepath)) and (("Drone" in filepath) or ("Voi" in filepath)) :  

            if os.path.getsize(filepath) >  1000000:

                ethcont.append(filepath)

print("")

print("Gathering Root Sounds.")

print("")

x = len(ethcont)

for ctr in range(50):
    y = random_number(x)
    atrack = ethcont[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Pystutter\\' + str(ctr) + tracknam + ".wav"
    print("")
    print("Copying: ", trackname)
    print("")
    shutil.copy(ethcont[y], outstr)

print("")

print("Initiating Stutter Code.")

print("")

print("This may take a few minutes.")

print("")

call(["python", "pystutr.py"])

## THE GHOST OF THE SHADOW ##
