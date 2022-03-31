#trieda macka
"""
class cat:
    #konštruktor = Vykona vždy keď vytvaram inštaciu triedy
    def __init__(self, meno, vek):
        print("vytvaram objekt macky")
        self.meno = meno
        self.vek = vek

    def __str__(self):
        print("meno macky je" + self.meno)
        print("vek macky je" + str(self.vek))


    def zamnaukaj(self):
        print(self.meno + "mnau")

    def zjedz(self, jedlo):
        print(self.meno + "zjedla/zjedol" + jedlo)


#vytvorenie inštacie objektu macka
Cat = cat("Mica", 4)
#Cat.meno = "cica"
Cat.zjedz("rybu")

#zvolanie metody
Cat.zamnaukaj()

cat2 = cat("Murko", 5)
cat2.meno = "Murko"
cat2.zamnaukaj()

print(cat2)
"""
from random import randint

"""
class car:
    def __init__(self, značka, rok_Vyroby, farba, počet_miest, jeNastartované):
        self.znacka = značka
        self.rokVyroby = rok_Vyroby
        self.farba = farba
        self.početmiest = počet_miest
        self.jenastartovane = jeNastartované


    def __str__(self):
        print("Značka auta je " +  self.znacka)
        print("Rok výroby je " +str(self.rokVyroby))
        print("Farba auta je " + self.farba)
        print("počet miest v aute je " +str(self.početmiest))
        return "";

    def zatrub(self):
        print("TUTU")

    def chodvpred(self):
        print("auto ide do predu")

    def nastartuj(self):
        print("BRM")


auto = car("Audi", 2018, "čierna", 5, "Nie")
auto.nastartuj()
auto.zatrub()
auto.chodvpred()
print(auto)
"""
"""
class kalkulacka:
    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2

    def sucet(self):
        sucet = self.cislo1 + self.cislo2
        print("Sucet je: ", sucet)
    def rozdiel(self):
        rozdiel = self.cislo1 - self.cislo2
        print("Rozdiel je: ", rozdiel)
    def sučin(self):
        sucin = self.cislo1 * self.cislo2
        print("Sucin je: ", sucin)
    def podiel(self):
        podiel = self.cislo1 / self.cislo2
        print("Podiel je: ", podiel)

cislo1 = int(input("Zadaj cislo 1:", ))
cislo2 = int(input("Zadaj cislo 2:", ))

kalkulacka = kalkulacka(10, 5)
kalkulacka.sucet()
kalkulacka.rozdiel()
kalkulacka.podiel()
kalkulacka.sučin()

"""

class Kocka:
    def __init__(self, strany):
        self.strany = strany

    def hod(self, hody):
        for i in range(hody):
            cislo = randint(1, self.strany)
            print(str(cislo) + " ", end = "")

kocka = Kocka(6)
kocka.hod(10)
print()
kocka2 = Kocka(4)
kocka2.hod(10)




