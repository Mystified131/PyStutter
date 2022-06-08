import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from pydub.utils import make_chunks
import numpy as np
import math

def reduce_volume(atrack, trvol):

    stsound = -22

    if trvol < stsound:
        chvol = (stsound - trvol)
        atrack = atrack + chvol

    if trvol > stsound:
        chvol = (trvol - stsound)
        atrack = atrack - chvol

    return atrack

def bass_line_freq(track):
    #sample_track = list(track)

    # c-value
    est_mean = np.mean(track)

    # a-value
    est_std = 3 * np.std(track) / (math.sqrt(2))

    bass_factor = int(round((est_std - est_mean) * 0.005))

    return bass_factor

def get_loudness(sound, slice_size):
    return max(chunk.dBFS for chunk in make_chunks(sound, slice_size))

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms
    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0  # ms
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size

    return trim_ms

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
        
        sound = AudioSegment.from_file(atrack)

        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())

        duration = len(sound)
        newAudio = sound[start_trim:duration-end_trim]
        #trimmed_sound.export(sys.argv[1], format="wav")
                
        attenuate_db = 0
        accentuate_db = .24
        #goldsound = -18
        goldsound = -15
        stsound = -23

        leng = len(newAudio)

        startvol = get_loudness(newAudio, leng)

        if (startvol < -11 and startvol > -18.5) and leng > 100000:

            newAudio2 = reduce_volume(newAudio, startvol)

            #filtered = newAudio2.low_pass_filter(bass_line_freq(newAudio2.get_array_of_samples()))

            #newAudio3 = (newAudio2 - attenuate_db).overlay(filtered + accentuate_db)

            loudn = get_loudness(newAudio2, leng)

            print(loudn)

            if loudn <= goldsound:
                chvol = (goldsound - loudn)
                newAudio = newAudio2 + chvol

            if loudn > goldsound:
                chvol = (loudn - goldsound)
                newAudio = newAudio2 - chvol
      
        audlen = len(newAudio)

        #Two Line For Secant Project

        #audlena = audlen - 80000

        #newAudio = newAudio[audlena:audlen]

        if audlen > 40000:

            chopAudio = newAudio[20000:40000]

            chopAudio2 = newAudio[15000:30000]

        if audlen < 50001:

            try:

                chopAudio = newAudio[10000:audlen]

                spot2 = audlen - 5000

                chopAudio2 = newAudio[5000:spot2]

            except:

                chopAudio = newAudio

                chopAudio2 = newAudio

                print("")

                print("Processing Error.")

                print("")

        #Volhardtweak optional

        #vb = -2

        #chopAudio += vb

        #chopAudio2 += vb

        try:

            oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Choppedout_" + trnam[y] + "_" + str(tim) + ".wav"
            chopAudio.export(oufil, format="wav")

        except:

            print("")

            print("Export error. File not rendered.")

            print("")

        try:

            oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\Choppedout_" + trnam[y] + "_2_"   + str(tim) + ".wav"
            chopAudio2.export(oufil, format="wav")

        except:

            print("")

            print("Export error. File not rendered.")

            print("")


print("")

print("Your chopped file(s) can be found in the same folder as this code.")

print("")

##THE GHOST OF THE SHADOW##







