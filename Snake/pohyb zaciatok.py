import random
import pygame

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

sirka_hada = 20
dlzka_hada = 20
velkost_jablka = 20

typ_pismen = pygame.font.SysFont('bitstreamverasans', 20)
typ_pismen2 = pygame.font.SysFont('bitstreamverasans', 150)

suradnicaX = int(random.randrange(100, 400))
suradnicaY = int(random.randrange(100, 300))

suradnica_jablkoX = int(random.randrange(100, 400))
suradnica_jablkoY = int(random.randrange(100, 300))

smer_hada = "hore"

suradnica_textX = 30
suradnica_textY = 15

suradnica_textX2 = 0
suradnica_textY2 = 0

prehra = False

while not prehra:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            suradnicaX -= 20
        elif key[pygame.K_RIGHT]:
            suradnicaX += 20
        elif key[pygame.K_UP]:
            suradnicaY -= 20
        elif key[pygame.K_DOWN]:
            suradnicaY += 20
    had = pygame.draw.rect(plocha, modra, [suradnicaX, suradnicaY, sirka_hada, dlzka_hada])

    jablko = pygame.draw.rect(plocha, cervena,
                                [suradnica_jablkoX, suradnica_jablkoY, velkost_jablka, velkost_jablka])

    if suradnicaX+-10 == suradnica_jablkoX+-10 and suradnicaY+-10 == suradnica_jablkoY+-10:
        body += 1
        dlzka_hada += 20

    vypisanie_textu = typ_pismen.render("Score: " + str(body), True, black)
    plocha.blit(vypisanie_textu, (suradnica_textX, suradnica_textY))

    pygame.display.update()
    cas.tick(25)

while prehra:
    vypisanie_textu2 = typ_pismen.render("GAME OVER ", True, black)
    plocha.blit(vypisanie_textu2, (suradnica_textX2, suradnica_textY2))

    pygame.quit()
    quit()




