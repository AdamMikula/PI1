import math

import pyglet

window = pyglet.window.Window(width=640, height=500)

def tik(T):
    had.x = had.x + T * 100
    had.y = 20 + 20 * math.sin(had.x/ 5)


def spracuj_text(text):
    had.x = 150

obrozok = pyglet.image.load("had.jfif")
had = pyglet.sprite.Sprite(obrozok)

def vykresli():
    window.clear()
    had.draw()

obrozok2 = pyglet.image.load("had 2.jfif")

def zmen(t):
    had.image = obrozok2
    pyglet.clock.schedule_once(zmenspat, 3)

def zmenspat(t):
    had.image = obrozok
    pyglet.clock.schedule_once(zmen, 3)

pyglet.clock.schedule_once(zmen, 3)

def klik(x,y,tlacitko, mod):
    had.x = x
    had.y = y
    print(x)
    print(y)
    print(tlacitko)
    print(mod)



window.push_handlers(on_text=spracuj_text,on_draw=vykresli,on_mouse_press=klik)
pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()

