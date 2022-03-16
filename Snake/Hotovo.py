import random
import pygame
import time

pygame.init()
sirka = 500
vyska = 400

cas = pygame.time.Clock()

zelena = (204,255,153)
silno_modra = (0,0,255)
modra = (0,255,255)
black = (0,0,0)
cervena = (255, 0, 0)

plocha = pygame.display.set_mode((sirka, vyska,))

pygame.display.update()

velkost_hada = 10
velkost_jablka = 10
dlzka_hada = 10

typ_pismen = pygame.font.SysFont('bitstreamverasans', 20)
typ_pismen2 = pygame.font.SysFont('bitstreamverasans', 100)

suradnicaX = 300
suradnicaY = 200

suradnica_jablkoX = random.randrange(10, (sirka//10))*10
suradnica_jablkoY = random.randrange(10, (vyska//10))*10

audio1 = pygame.mixer.Sound("jedenie.mp3.mp3")
audio2 = pygame.mixer.Sound("naraz.mp3")
audio3 = pygame.mixer.Sound("game over.mp3")

hodiny = pygame.time.Clock()

suradnice_hada = [suradnicaX, suradnicaY]

suradnica_textX = 30
suradnica_textY = 15

dx = 0
dy = 0

suradnica_textX2 = 0
suradnica_textY2 = 150

suradnica_textX3 = 190
suradnica_textY3 = 250

body = 0

prehra = False

while not prehra:
    plocha.fill(zelena)

    had = pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, velkost_hada, dlzka_hada])

    jablko = pygame.draw.rect(plocha, cervena,
                              [suradnica_jablkoX, suradnica_jablkoY, velkost_jablka, velkost_jablka])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx -= 10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx += 10
                dy = 0
            elif event.key == pygame.K_UP:
                dy -= 10
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy += 10
                dx = 0
    suradnicaX += dx
    suradnicaY += dy

    if suradnicaY < 395 and suradnicaY > -1 and suradnicaX < 495 and suradnicaX > -1:
        prehra = False
    else:
        prehra = True
        pygame.mixer.Sound.play(audio2)

    if suradnicaX == suradnica_jablkoX and suradnicaY == suradnica_jablkoY:
        body += 1
        suradnica_jablkoX = random.randrange(1, (sirka // 10)) * 10
        suradnica_jablkoY = random.randrange(1, (vyska // 10)) * 10
        pygame.mixer.Sound.play(audio1)

    vypisanie_textu = typ_pismen.render("Počet bodov: " + str(body), True, silno_modra)
    plocha.blit(vypisanie_textu, (suradnica_textX, suradnica_textY))

    hodiny.tick(15)

    pygame.display.update()

if prehra:
    time.sleep(1)
    pygame.mixer.Sound.play(audio3)

while prehra:
    plocha.fill(zelena)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    vypisanie_textu2 = typ_pismen2.render("GAME OVER ", True, cervena)
    plocha.blit(vypisanie_textu2, (suradnica_textX2, suradnica_textY2))

    vypisanie_textu3 = typ_pismen.render("Tvoj počet bodov: "+str(body), True, cervena)
    plocha.blit(vypisanie_textu3, (suradnica_textX3, suradnica_textY3))

    pygame.display.update()


