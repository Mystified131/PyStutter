import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

for reps in range(1):

    choptrax = []

    trnam = []

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\PyStutter'):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav"):
                choptrax.append(filepath)
                trnam.append(str(file[:-4]))

    trlen = len(choptrax)

    for y in range(trlen):

        atrack = choptrax[y]

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

        #Two Line For Secant Project

        audlena = audlen - 80000

        newAudio = newAudio[audlena:audlen]

        if audlen > 50000:

            chopAudio = newAudio[20000:50000]

        if audlen < 50001:

            try:

                chopAudio = newAudio[10000:audlen]

            except:

                print("")

                print("Processing Error.")

                print("")

        #Volboost optional

        vb = 2

        chopAudio += vb

        try:

            oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Choppedout_" + trnam[y] + "_" + str(tim) + ".wav"
            chopAudio.export(oufil, format="wav")

        except:

            print("")

            print("Export error. File not rendered.")

            print("")

print("")

print("Your chopped file(s) can be found in the same folder as this code.")

print("")

##THE GHOST OF THE SHADOW##







