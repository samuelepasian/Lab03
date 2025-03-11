class Dictionary:
    def __init__(self):
        self._dict=[]

    def addWord(self,parola):
        self._dict.append(parola)

    def loadDictionary(self,path):
        nome=f"resources/{path}.txt"
        with open(nome, "r") as dizionario:
            file = dizionario.readlines()
        dict = Dictionary()
        for riga in file:
            self.addWord(riga[:-1])
        return dict


    def printAll(self):
        for parola in self._dict:
            print(parola)


    @property
    def dict(self):
        return self._dict

