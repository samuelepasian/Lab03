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
        diz.loadDictionary(language)
        for parola in parole:
            giusta = False
            richword = rw.RichWord(parola)
            if parola in diz.dict:
                giusta=True
            richword.corretta=giusta
            rwords.append(richword)
        return rwords

    def searchWordLinear(self, words, language):
        rwords = []
        parole = words.split()
        diz = d.Dictionary()
        diz.loadDictionary(language)
        for parola in parole:
            giusta = False
            richword = rw.RichWord(parola)
            for elemento in diz.dict:
                if richword._parola==elemento:
                    giusta=True
                    break
            richword.corretta=giusta
            rwords.append(richword)
        return rwords

    def searchWordDichotomic(self, words, language):
        rwords = []
        parole = words.split()
        diz = d.Dictionary()
        diz.loadDictionary(language)
        indice=len(diz.dict)//2
        elementoCentale=diz.dict[indice]
        for parola in parole:
            giusta = False
            richword=rw.RichWord(parola)
            if parola>elementoCentale:
                count=indice
                while count<len(diz.dict) and giusta==False:
                    if diz.dict[count]==parola:
                        giusta=True
                    else:
                        count+=1
            if parola<elementoCentale:
                count =0
                while count < indice and giusta == False:
                    if diz.dict[count] == parola:
                        giusta = True
                    else:
                        count += 1
            richword.corretta=giusta
            rwords.append(richword)
        return rwords



