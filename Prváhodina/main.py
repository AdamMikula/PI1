
"""
Vek = int(input("Zadaj svoj vek"))

if Vek >= 18:
    print("mozes ist dalej")
else:
     print("nemozes si mac mladý")
"""

"""
Password = (input("Zadaj svoje heslo: "))

if Password == "adam":
    print("si medzi nami")
else:
    print("si blbec maš zlé heslo")
"""
"""
X = int(input("zadaj prvé číslo: "))
Y = int(input("zadaj druhé číslo: "))

print("výsledok násobenia sa rovná: ", X*Y)
print("výsledok delenia sa rovná: ", X/Y)
print("výsledok súčtu sa rovná: ", X+Y)
print("výsledok rozdielu sa rovná: ", X-Y)
"""

"""
start = 100
koniec = 0
while start >= koniec:
    print(start)
    start = start - 5
"""
"""
start = 10
koniec = 0
while start >= koniec:
    if start == 5:
        break
    print(start)
    start -= 1
"""
"""
x = int(input("zadajte zaciatocne cislo :"))
y = int(input("zadajte koncove cislo :"))
while(x < y):
    if(x % 3 == 0):
        print(x, "je nasobok 3ky")
     x += 1
"""
"""
for premenny in range(10):
    print(premenny)
   
"""
"""
samohlasky = "aáeéiíoóuúyý"
slovo = input("zadaj slovo: ")
obsahuje_sam = False
for znak in slovo:
    if znak in samohlasky:
        obsahuje_sam = True
        break

if obsahuje_sam == True:
    print("slovo obsahuje samohlasky")
else:
    print("slovo neobsahuje samohlasky")
while 
"""
"""
znaky = "?!%+-*/><._-,:()§ä=ˇ°"
samohlasky = "aáeéiíoóuúyý"
spoluhlásky = "dtnlchgkďťňjľcčžšdzdžmbpvzsfr"
cisla = "12345678910"
slovo = input("zadaj slovo: ")
pocet_samohlasok = 0
pocet_spoluhlasok = 0
pocet_cisel = 0
pocet_znakov = 0
for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok += 1
    if znak in spoluhlásky:
        pocet_spoluhlasok += 1
    if znak in cisla:
        pocet_cisel +=1
    if znak in znaky:
        pocet_znakov +=1
if pocet_samohlasok > 0:
    print("slovo obsahuje samohlasky", pocet_samohlasok)
else:
    print("slovo neobsahuje samohlasky")
if pocet_spoluhlasok > 0:
    print("slovo obsahuje spoluhlasok", pocet_spoluhlasok)
else:
    print("slovo neobsahuje spoluhlásky")
if pocet_cisel > 0:
    print("slovo obsahuje cisel", pocet_cisel)
else:
    print("slovo neobsahuje cisla")
if pocet_znakov > 0:
    print("slovo obsahuje znakov",pocet_znakov)
else:
    print("slovo neobsahuje znaky")
"""


















