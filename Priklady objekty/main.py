"""
class Clovek:
    def __init__(self, meno):
        self.meno = meno
        self.unava = 0
        self.limitunava = 20
        print(self)

    def beh(self, km):
        if km > self.limitunava - self.unava:
            return
        self.unava += km
        print(self)

    def spanok(self, hodiny):
        self.unava -= hodiny * 10
        if self.unava < 0:
            self.unava = 0
        print(self)

clovek = Clovek("Karol")
clovek.beh(5)
clovek.spanok(10)
"""
"""
import random

class Vety:
    def __init__(self):
        self.privlastok = ["malý", "velky", "silný", "slabý"]
        self.podmet = ["policajt", "právnik", "hroch", "pes"]
        self.predlozka = ["s radosťou", "bez radosti"]
        self.prisudok = ["upratoval", "spal", "varil", "piekol"]
        self.prisudzovaci = ["u sestry" ,"u babičky", "v potoku"]

    def vyber(self):
        slovo = random.choice(self.privlastok)
        slovo2 = random.choice(self.podmet)
        slovo3 = random.choice(self.predlozka)
        slovo4 = random.choice(self.prisudok)
        slovo5 = random.choice(self.prisudzovaci)
        print(slovo + " " +  slovo2 + " " + slovo3 + " " +  slovo4 + " "+  slovo5)

vety = Vety()
vety.vyber()
"""

class Garaz():
    auta_v_garazi = []

    def vypis_aut(self):
        if self.auta_v_garazi == []:
            print("garaz je prazdna")
        else:
            print("v garazi su auta: {} ".format(", ".join(self.auta_v_garazi)))

class auto():

    def __init__(self, SPZ, farba):
        self.SPZ =SPZ
        self.farba = farba

    def zaparkuj(self, garage):
        garage.auta_v_garazi.append("{0} {1}".format(self.SPZ, self.farba))

    def vyparkuj(self, garage):
        garage.auta_v_garazi.remove("{0} {1}".format(self.SPZ, self.farba))

garaz = Garaz()
audi = auto("ZA111", "cierna")
audi.zaparkuj(garaz)
mercedes = auto("Ca111", "siva")
mercedes.zaparkuj(garaz)
mercedes.vyparkuj(garaz)
garaz.vypis_aut()




