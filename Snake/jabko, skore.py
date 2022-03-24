import random
import pygame

pygame.init()
sirka = 500
vyska = 400

zelena = (204,255,153)
silno_modra = (0,0,255)
modra = (0,255,255)
black = (0,0,0)
cervena = (255, 0, 0)

Skore = 0

plocha = pygame.display.set_mode((sirka, vyska))
plocha.fill(zelena)
pygame.display.update()

velkost_hada = 15
rychlost_hada = 20

typ_pismen = pygame.font.SysFont('bitstreamverasans', 20)
typ_pismen2 = pygame.font.SysFont('bitstreamverasans', 150)

suradnicaX = random.randrange(100, 400)
suradnicaY = random.randrange(100, 300)

suradnica_jablkoX = random.randrange(1, (suradnicaX//10)) * 10
suradnica_jablkoY = random.randrange(1, (suradnicaY//10)) * 10

suradnica_textX = 30
suradnica_textY = 15

suradnica_textX2 = 0
suradnica_textY2 = 0

prehra = False

while not prehra:
    had = pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, velkost_hada, velkost_hada + 15])

    jablko = pygame.draw.rect(plocha, cervena, [suradnica_jablkoX, suradnica_jablkoY, velkost_hada, velkost_hada])

    vypisanie_textu = typ_pismen.render("Score: ", True, black)
    plocha.blit(vypisanie_textu, (suradnica_textX, suradnica_textY))

    pygame.display.update()

while prehra:
    vypisanie_textu2 = typ_pismen.render("GAME OVER ", True, black)
    plocha.blit(vypisanie_textu2, (suradnica_textX2, suradnica_textY2))

    pygame.quit()
    quit()




