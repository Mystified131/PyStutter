import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

for reps in range(3):

    stuttertrax = []

    trnam = []

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyStutter'):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav") and ('AtmosOut' not in str(filepath)) and ('VoxOut' not in str(filepath)) and ('SoundsOut' not in str(filepath)):
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

                oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Stutterout_" + trnam[y] + "_" + str(tim) + ".wav"
                altAudio.export(oufil, format="wav")
    
        oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Stutterout_" + trnam[y] + "_" + str(tim) + ".wav"    
        altAudio.export(oufil, format="wav")


for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")) and ('AtmosOut' not in str(filepath)) and ('VoxOut' not in str(filepath)) and ('SoundsOut' not in str(filepath)):
            #os. remove(filepath) 
            print("")


##THE GHOST OF THE SHADOW##







