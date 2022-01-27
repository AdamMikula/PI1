#KONSTANTY OKNA
from distutils.command.install import key

import pyglet
import random
from pyglet import gl

SIRKA = 500
VYSKA = 350

#LOPTA
VELKOST_LOPTY= 20
RYCHLOST = 300 #pixely za sekundu

#PALKY
TLSTKA_PALKY = 10
VYSKA_PALKY = 100
RYCHLOST_PALKY =  RYCHLOST * 1.5


#PROSTREDNA CIARA
CIARA_HRUBKA = 20

#FONT
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#STAVOVE PREMENEN
pozicia_palok = [VYSKA //2, VYSKA//2]
pozicia_lopty = [SIRKA//2,VYSKA//2]
rychlost_lopty =[0,0]
stisknute_klavesy = set()
skore = [0,0]

#
def reset():
    pozicia_lopty[0] = SIRKA//2
    pozicia_lopty[1] = VYSKA//2

    if random.randint(0,1):
        rychlost_lopty[0] = RYCHLOST
    else:
        rychlost_lopty[0] = -RYCHLOST

    rychlost_lopty[1] = random.uniform(-1,1) * RYCHLOST

"""
Nakresli obdelnik na dane souradnice
Nazorny diagram::
     y2 - +-----+
          |/////|
     y1 - +-----+
          :     :
         x1    x2
"""
def vykresli_obdlznik(x1,y1, x2,y2):
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku

def nakresli_text(text, x, y, pozice_x):
    """Nakresli dany text na danou pozici
    Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
    bude text zarovnany
    """
    napis = pyglet.text.Label(text,font_size=VELKOST_FONTU,x=x,y=y,anchor_x=pozice_x)
    napis.draw()

def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add( ("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.add( ("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.add( ("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add( ("dole", 1))

def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard( ("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.discard( ("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.discard( ("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard( ("dole", 1))


def vykresli():
    """Vykresli stav hry"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou

    #Vykresli loptu
    vykresli_obdlznik(
       pozicia_lopty[0] - VELKOST_LOPTY //2,
       pozicia_lopty[1] - VELKOST_LOPTY //2,
       pozicia_lopty[0] + VELKOST_LOPTY //2,
       pozicia_lopty[1] + VELKOST_LOPTY //2
    )

    #Vykreslit palky
    # palky - udelame si seznam souradnic palek a pro kazdou dvojici souradnic
    # v tom seznamu palku vykreslime
    for x, y in [(0, pozicia_palok[0]), (SIRKA, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY // 2,
            x + TLSTKA_PALKY,
            y + VYSKA_PALKY // 2,
        )

    #Vykreslenie: Poliacia ciara
    # prerusovana pulici cara - slozena ze spousty malych obdelnicku
    for y in range(CIARA_HRUBKA // 2, VYSKA, CIARA_HRUBKA * 2):
        vykresli_obdlznik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + CIARA_HRUBKA
        )

    #vykreslit score
    nakresli_text(str(skore[0]),x=ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='left')
    nakresli_text(str(skore[1]),x=SIRKA-ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='right')

    print(stisknute_klavesy)

def obnov_stav(dt):
    for cislo_palky in (0,1):
        if ("hore", cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] += RYCHLOST_PALKY * dt
        if ("dole", cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] -= RYCHLOST_PALKY * dt

        if pozicia_palok[cislo_palky] < VYSKA_PALKY /2:
            pozicia_palok[cislo_palky] = VYSKA_PALKY/2

        if pozicia_palok[cislo_palky] > VYSKA - VYSKA_PALKY /2:
            pozicia_palok[cislo_palky] = VYSKA - VYSKA_PALKY /2

    pozicia_lopty[0] += rychlost_lopty[0] * dt
    pozicia_lopty[1] += rychlost_lopty[1] * dt

    if pozicia_lopty[1] < VELKOST_LOPTY:
        rychlost_lopty[1] = abs(rychlost_lopty[1])

    if pozicia_lopty[1] > VYSKA - VELKOST_LOPTY:
        pozicia_lopty[1] = -abs(rychlost_lopty[1])

    palka_min = pozicia_lopty[1] - VELKOST_LOPTY / 2 -  VYSKA_PALKY / 2
    palka_max = pozicia_lopty[1] + VELKOST_LOPTY / 2 - VYSKA_PALKY / 2

    if pozicia_lopty[0] < TLSTKA_PALKY + VELKOST_LOPTY/2:
        if palka_min < pozicia_palok[0] < palka_max:
            rychlost_lopty[0] = abs(rychlost_lopty[0])
        else:
            skore[1] += 1
            reset()

    if pozicia_lopty[0] > SIRKA - (TLSTKA_PALKY + VELKOST_LOPTY / 2):
        if palka_min < pozicia_palok[1] < palka_max:
            rychlost_lopty[0] = -abs(rychlost_lopty[0])
        else:
            skore[1] += 1
            reset()


reset()
window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice,
)
pyglet.clock.schedule(obnov_stav)
pyglet.app.run()
