import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        testo=replaceChars(txtIn)
        multidic=md.MultiDictionary()
        startTime = time.time()
        parole=multidic.searchWord(testo,language)
        endTime = time.time()
        tempo = endTime - startTime
        print("Using contains")
        for parola in parole:
            if parola._corretta==False:
                print(parola)
        print(f"{tempo}\n")

        startTime2 = time.time()
        parole2 = multidic.searchWordLinear(testo, language)
        endTime2 = time.time()
        tempo2 = endTime2 - startTime2
        print("Using Linear search")
        for parola in parole2:
            if parola._corretta == False:
                print(parola)
        print(f"{tempo2}\n")

        startTime3 = time.time()
        parole3 = multidic.searchWordDichotomic(testo, language)
        endTime3 = time.time()
        tempo3 = endTime3 - startTime3
        print("Using Dichotomic search")
        for parola in parole3:
            if parola._corretta == False:
                print(parola)
        print(f"{tempo3}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")




def replaceChars(text):
    testo=text.lower()
    chars="\\'*_{}[]()>#+-.$%^;,="
    for c in chars:
        testo=testo.replace(c,"")
    return testo