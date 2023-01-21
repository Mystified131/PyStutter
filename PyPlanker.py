import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

for reps in range(1):

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

        segnum = 24

        sllen = int(0) + 7
        
        audlen = int(audlen / segnum)

        SilAudio = AudioSegment.silent(duration = sllen)

        OutAud = newAudio[0:0]

        for iter in range(segnum):

            stval = iter * audlen
            enval2 = stval + audlen
            enval = stval + (audlen - sllen)

            SlicAud = newAudio[stval:enval]

            Slic1Aud = SlicAud.fade_in(5)

            Slic2Aud = Slic1Aud.fade_out(2)

            CutAud = Slic2Aud + SilAudio

            OutAud += CutAud

        #Create Longer Phrase

        measnum = 16

        EndAud = OutAud * measnum

        try:

            oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Plankerout_" + trnam[y] + "_" + str(tim) + ".wav"
            EndAud.export(oufil, format="wav")

        except:

            print("")

            print("Planker Creation Failure For: ", trnam[y])


##THE GHOST OF THE SHADOW##







