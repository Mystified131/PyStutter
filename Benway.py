import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

for reps in range(3):

    benwaytrax = []

    trnam = []

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyStutter'):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav") and ('AtmosOut' not in str(filepath)) and ('VoxOut' not in str(filepath)) and ('SoundsOut' not in str(filepath)):
                benwaytrax.append(filepath)
                trnam.append(str(file[:-4]))

    trlen = len(benwaytrax)

    for y in range(trlen):

        atrack = benwaytrax[y]

        print("")

        print("Please wait. Working on: " + atrack)

        print("")
            
        newAudio = AudioSegment.from_wav(atrack)

        audlen = len(newAudio)

        if audlen < 3001 or audlen > 1000000:

            print("")

            print("Audio wrong length. Please use .wav files between 3 and 100 seconds in length.")

            print("")

        if audlen > 3000 and audlen < 1000001:

            right_now = datetime.datetime.now().isoformat()
            list = []

            for i in right_now:
                if i.isnumeric():
                    list.append(i)

            tim = ("".join(list))

            outAudio = newAudio[0:0]

            bennum = random_number2(18, 42)

            for ctr in range(bennum):

                ranval1 = random_number(audlen - 2900)

                ranval2 = random_number2(ranval1, audlen)

                ranquot = random_number2(1, 6)

                ranvaltrunc = int(ranval2 / ranquot)

                newSeg = newAudio[ranval1:ranvaltrunc]

                newSeg = newSeg.fade_in(10)

                newSeg = newSeg.fade_out(10)

                outAudio += newSeg

            oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Benwayout_" + trnam[y] + "_" + str(tim) + ".wav"
            outAudio.export(oufil, format="wav")

##THE GHOST OF THE SHADOW##







