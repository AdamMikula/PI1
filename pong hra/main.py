import pyglet
from pyglet import gl

sirka_okna = 1000
vyska_okna = 700

velkost_lopty = 20
RYCHLOST_LOPTY_PIXELY = 200

tlstka_palky = 10
vyska_palky = 100
RYCHLOST_PALKY = RYCHLOST_LOPTY_PIXELY * 1.5



hrubka_ciary = 20

VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

pozicia_palok = [vyska_okna//2, vyska_okna//2]
pozicia_lopty = [0,0]
rychlost_lopty = [0,0]
stisknute_klavesy = set()
skore = [0,0]

def nakresli_text(text x, y):
    napis = pyglet.text.lable(
        text,
        font_size = VELKOST_FONTU,
        x=x,
        y=y,
        anchor_x = pozice_x,


    )
    napis.draw()




def vykresli_obdlznik(x1,y1, x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # u

def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)
    vykresli_obdlznik(
        pozicia_lopty[0] - velkost_lopty//2,
        pozicia_lopty[1] - velkost_lopty//2,
        pozicia_lopty[0] + velkost_lopty//2,
        pozicia_lopty[1] + velkost_lopty//2
    )

    for x, y in [(0, pozicia_palok[0]), (sirka_okna, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - tlstka_palky //2,
            x + tlstka_palky,
            y + vyska_palky //2
        )

    for y in range(hrubka_ciary //2, vyska_okna, hrubka_ciary * 2):
        vykresli_obdlznik(
            sirka_okna //2 -1,
            y,
            sirka_okna //2 + 1,
            y + hrubka_ciary
        )






    nakresli_text(str(skore[0]),x=ODSADENIE_TEXTU,y = vyska_okna- ODSADENIE_TEXTU - VELKOST_FONTU,
                  pozice_x="left"
                  )
    nakresli_text(str(skore[1]),x=sirka_okna - ODSADENIE_TEXTU ,y = vyska_okna - ODSADENIE_TEXTU - VELKOST_FONTU,
                  pozice_x="right"
                  )





window = pyglet.window.Window(width = sirka_okna,height = vyska_okna)
window.push_handlers(on_draw=vykresli,)






pyglet.app.run()



