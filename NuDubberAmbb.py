#This code imports the necessary modules.

import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from pydub.utils import make_chunks
import numpy as np
import math
from subprocess import call
import shutil

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

repper = 3

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

outfile = open('AutoPlayListPepper.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsamplepepper" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


outfile = open('AutoPlayListDrones.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsampledrone" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


infile = open("AutoPlayListDrones.m3u", "r")

contentdrones = []

plist = infile.readline()
while plist:
    contentdrones.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListPepper.m3u", "r")

contentpepper = []

plist = infile.readline()
while plist:
    contentpepper.append(plist)
    plist = infile.readline()
infile.close()

trtot = 50

suctot = 0

for ctr in range(700):

    try:

        ####################################################### #1

        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        print("")

        print("Layering tracks for track: ", (suctot + 1))

        
        newAudio2 = AudioSegment.from_wav(atrack3) 
        l2 = len(newAudio2)

        newAudiow2 = newAudio2 * repper
        totlen = len(newAudio2)

        newAudio3 = AudioSegment.from_wav(atrack4) 
        l2 = len(newAudio3)
        rep = int(totlen / l2)

        newAudiox = newAudio3*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudionear1 = newAudioamb2 * 2

        ############################################################ #2

        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        newAudio2 = AudioSegment.from_wav(atrack3) 
        l2 = len(newAudio2)

        newAudiow2 = newAudio2 * repper
        totlen = len(newAudio2)

        newAudio3 = AudioSegment.from_wav(atrack4) 
        l2 = len(newAudio3)
        rep = int(totlen / l2)

        newAudiox = newAudio3*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudionear2 = newAudioamb2 * 2


        ############################################################ #3


        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        newAudio2 = AudioSegment.from_wav(atrack3) 
        l2 = len(newAudio2)
        
        newAudiow2 = newAudio2 * repper
        totlen = len(newAudio2)

        newAudio3 = AudioSegment.from_wav(atrack4) 
        l2 = len(newAudio3)
        rep = int(totlen / l2)

        newAudiox = newAudio3*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudionear3 = newAudioamb2 * 2


        ############################################################


        oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\AtmosOut\\EthnoAtmos_1_" + tim + "." + str(suctot) + ".wav"
        newAudionear1.export(oufil, format="wav")

        oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\AtmosOut\\EthnoAtmos_2_" + tim + "." + str(suctot) + ".wav"
        newAudionear2.export(oufil, format="wav")

        oufil = "C:\\Users\\mysti\\Coding\\PyStutter\\AtmosOut\\EthnoAtmos_3_" + tim + "." + str(suctot) + ".wav"
        newAudionear3.export(oufil, format="wav")

        suctot += 1

        if suctot == trtot:
            break

    except:

        print("")

        print("Error during render. File not created.")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".ogg")) or (filepath.endswith(".wav")) or (filepath.endswith(".txt")) or (filepath.endswith(".sfk"))   and ("Generate" in str(filepath))  or ("GenCh" in str(filepath)) or ("vsamp" in str(filepath)) or ("newsound" in str(filepath)):
            os. remove(filepath) 

print("")

print("The designated files have been removed. Thank you.")

print("")

#call(["python", "C:\\Users\\mysti\\Coding\\Pystutter\\StartTrackEvolvingHere.py"])

call(["python", "BatchEthnoSoundsStut.py"])

## THE GHOST OF THE SHADOW ##
