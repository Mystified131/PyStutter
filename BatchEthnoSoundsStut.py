#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

#srchstr = 'E:\\EthnoSoundSources'

srchstr = 'H:\\Acid_Loops'

ethcont = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
         
        if  filepath.endswith(".wav") and (("Ethno" in filepath) or ("World" in filepath)) and (("Drone" in filepath) or ("Voi" in filepath)) :  

            if os.path.getsize(filepath) >  1000000:

                ethcont.append(filepath)

print(ethcont)

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
    outstr = 'C:\\Users\\mysti\\Coding\\Pystutter\\SoundsOut' + "EthnoSounds" +  str(ctr) + tracknam +  '.wav'

    print("")
    print("Copying: ", trackname)
    print("")
    shutil.copy(ethcont[y], outstr)

print("")

print("Initiating Stutter Code.")

print("")

print("This may take a few minutes.")

print("")

for reps in range(3):

    stuttertrax = []

    trnam = []

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyStutter\\SoundsOut'):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav") :
                stuttertrax.append(filepath)
                trnam.append(str(file[:-4]))

    trlen = len(stuttertrax)

    for y in range(trlen):

        atrack = stuttertrax[y]

        right_now = datetime.datetime.now().isoformat()
        list = []

        for i in right_now:
            if i.isnumeric():
                list.append(i)

        tim = ("".join(list))

        print("")

        print("Please wait. Working on: " + atrack)

        print("")
            
        newAudio = AudioSegment.from_wav(atrack)

        audlen = len(newAudio)

        slen = random_number2(1000,3000)

        slctot = (int(audlen/slen))

        slpt = 0

        altAudio = newAudio[0:0]

        for ctr in range(slctot):

            try:

                slen = random_number2(1000,3000)

                slend = slpt + slen

                altAudio = altAudio + newAudio[slpt:slend]

                sttr = random_number2(50, 225)

                sttrinc = random_number2(3, 6)

                sval = slend - sttr

                stutAud = newAudio[sval:slend]

                for ctr in range(sttrinc):

                    altAudio = altAudio + stutAud

                slpt  += slen

            except:

                print("")

                print("Process Termination")

                print("")

                oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\SoundsOut\\Stutterout_" + trnam[y] + "_" + str(tim) + ".wav"
                altAudio.export(oufil, format="wav")
    
        oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\SoundsOut\\Stutterout_" + trnam[y] + "_" + str(tim) + ".wav"    
        altAudio.export(oufil, format="wav")

call(["python", "BatchEthnoVoxStut.py"])

## THE GHOST OF THE SHADOW ##
