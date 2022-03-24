import random
import pygame


pygame.init()
sirka = 500
vyska = 400

zelena = (204,255,153)
modra = (0,255,255)
black = (0,0,0)

pygame.mixer.music.load()

plocha = pygame.display.set_mode((sirka, vyska))
plocha.fill(zelena)
pygame.display.update()
velkost_hada = 15
rychlost_hada = 20

typ_pismen = pygame.font.SysFont('bitstreamverasans', 20)


suradnicaX = random.randrange(100, 400)
suradnicaY = random.randrange(100, 300)

suradnicaX1 = 0
suradnicaY1 = 0

prehra = False
while not prehra:

    pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, velkost_hada, velkost_hada])

    pygame.display.update()


pygame.quit()
quit()

