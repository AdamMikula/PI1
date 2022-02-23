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

body = 0

plocha = pygame.display.set_mode((sirka, vyska,))
plocha.fill(zelena)
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

suradnica_textX2 = 0
suradnica_textY2 = 150
SMER = "hore"
zmena = SMER

prehra = False

while not prehra:
    pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, velkost_hada, dlzka_hada])

    jablko = pygame.draw.rect(plocha, cervena,
                              [suradnica_jablkoX, suradnica_jablkoY, velkost_jablka, velkost_jablka])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zmena = 'UP'
            if event.key == pygame.K_DOWN:
                zmena = 'DOWN'
            if event.key == pygame.K_LEFT:
                zmena = 'LEFT'
            if event.key == pygame.K_RIGHT:
                zmena = 'RIGHT'

    if zmena == 'UP' and SMER != 'DOWN':
        SMER = 'UP'
    if zmena == 'DOWN' and SMER != 'UP':
        SMER = 'DOWN'
    if zmena == 'LEFT' and SMER != 'RIGHT':
        SMER = 'LEFT'
    if zmena == 'RIGHT' and SMER != 'LEFT':
        SMER = 'RIGHT'

    if SMER == 'UP':
        if suradnicaY > 2:
            suradnicaY -= 10
        else:
            prehra = True
            pygame.mixer.Sound.play(audio2)
    if SMER == 'DOWN':
        if suradnicaY < 390:
            suradnicaY += 10
        else:
            prehra = True
            pygame.mixer.Sound.play(audio2)
    if SMER == 'LEFT':
        if suradnicaX > 2:
            suradnicaX -= 10
        else:
            prehra = True
            pygame.mixer.Sound.play(audio2)
    if SMER == 'RIGHT':
        if suradnicaX < 490:
            suradnicaX += 10
        else:
            prehra = True
            pygame.mixer.Sound.play(audio2)

    hodiny.tick(17)
    pygame.display.update()

    if suradnicaX+-5 == suradnica_jablkoX+-5 and suradnicaY+-5 == suradnica_jablkoY+-5:
        body += 1
        suradnica_jablkoX = random.randrange(1, (sirka // 10)) * 10
        suradnica_jablkoY = random.randrange(1, (vyska // 10)) * 10
        pygame.mixer.Sound.play(audio1)
        pygame.display.update()

    vypisanie_textu = typ_pismen.render(f"Score {body}", True, black)
    plocha.blit(vypisanie_textu, (suradnica_textX, suradnica_textY))
    pygame.display.update()

if prehra:
    time.sleep(1)
    pygame.mixer.Sound.play(audio3)

while prehra:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    vypisanie_textu2 = typ_pismen2.render("GAME OVER ", True, cervena)
    plocha.blit(vypisanie_textu2, (suradnica_textX2, suradnica_textY2))

    pygame.display.update()









