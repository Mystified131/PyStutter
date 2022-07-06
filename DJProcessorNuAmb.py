#This code imports the necessary modules.

from pydub import AudioSegment
import random
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

def add_stutter(newAudio):
    
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

            return altAudio

    return altAudio

def add_deelay(newAudio):
   
    audlen = len(newAudio)

    delln = random_number2(100, 800)

    delAudio = AudioSegment.silent(duration = delln)

    delitr = random_number2(4, 6)

    defad = 1 / delitr * 18

    defad2 = .4 * defad

    altAudio = newAudio - defad2

    altAudiodelt = newAudio[0:0]

    for ctr in range(delitr):

        altAudionew = delAudio + altAudio

        altAudionew = altAudionew - defad

        altAudio = altAudio + delAudio

        altAudiodelt = altAudionew.overlay(altAudio)

        altAudio = altAudiodelt - defad2

    return newAudio

contentdrones = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "drone" in str(filepath):
            cline = str(file)
            contentdrones.append(cline)

contentpepper = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Pystutter'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "pepper" in str(filepath):
            cline = str(file)
            contentpepper.append(cline)

print("Extracting samples. Please wait.")

print("")

sizlim = 15000000

print("Overlaying recording.")

for ctr in range(50):

    astr = ("Drone Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentdrones))
    atrack = contentdrones[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random_number(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(5000, 8000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            stutdic = random_number(10)
            if stutdic > 7:
                newAudio = add_stutter(newAudio)
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
            newvol = random_number2(14,20)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(100)
            newAudio = newAudio.fade_out(100)
            sil1 = random_number2(12000, 14000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(48000, 53000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(18,22)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(10000, 12000)
            sil2 = random_number2(12000, 13000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(40000, 42000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,18)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(8000, 9000)
            sil2 = random_number2(12000, 14000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(2000, 7000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,26)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            addAudio = newAudio
            ctr = random_number2(3,8)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(3000, 8000)
            sil2 = random_number2(6000, 8000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random_number(10)
        if dic == 7:
            sil1 = random_number(9000)
            sil2 = random_number(10000)
            newAudio = newAudio - 5
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\\Pystutter\\newsampledrone" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(50):

    astr = ("Other Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentpepper))
    atrack = contentpepper[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random_number(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(1600, 2400)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
            newvol = random_number2(8,12)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(4000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(8000, 24000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
            newvol = random_number2(12,18)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(6000)
            sil2 = random_number(12000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(50000, 52000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
            newvol = random_number2(10,14)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(10000)
            sil2 = random_number(8000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(200, 800)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
            newvol = random_number2(10,14)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(10)
            newAudio = newAudio.fade_out(10)
            addAudio = newAudio
            ctr = random_number2(3,8)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(6000)
            sil2 = random_number(8000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random_number(10)
        if dic == 7:
            sil1 = random_number(30000)
            sil2 = random_number(20000)
            newAudio = newAudio -3
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\\Pystutter\\newsamplepepper" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

call(["python", "NuDubberAmbb.py"])

## THE GHOST OF THE SHADOW ##