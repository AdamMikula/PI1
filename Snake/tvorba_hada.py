import random
import pygame


pygame.init()
sirka = 500
vyska = 400

plocha = pygame.display.set_mode((sirka, vyska))

velkost_hada = 15
rychlost_hada = 20

typ_pismen = pygame.font.SysFont('bitstreamverasans', 20)
modra = (0,255,255)
black = (0,0,0)


modra = (0,255,255)
black = (0,0,0)

suradnicaX = random.randrange(100, 400)
suradnicaY = random.randrange(100, 300)

suradnicaX1 = 0
suradnicaY1 = 0

prehra = False
while not prehra:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                suradnicaX1 = -10
                suradnicaY1 = 0
            if event.key == pygame.K_RIGHT:
                suradnicaX1 = 10
                suradnicaY1 = 0
            if event.key == pygame.K_UP:
                suradnicaX1 = 0
                suradnicaY1 = 10
            if event.key == pygame.K_DOWN:
                suradnicaX1 = 0
                suradnicaY1 = -10

    pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, velkost_hada, velkost_hada])

    pygame.display.update()


pygame.quit()
quit()

