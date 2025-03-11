import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        diz=d.Dictionary()
        diz.loadDictionary(language)
        diz.printAll()

    def searchWord(self, words, language):
        rwords=[]
        parole=words.split()
        diz=d.Dictionary()
        giusta=False
        diz.loadDictionary(language)
        for parola in parole:
            richword = rw.RichWord(parola)
            if parola in diz.dict:
                giusta=True
            richword.corretta=giusta
            rwords.append(richword)
        return rwords


