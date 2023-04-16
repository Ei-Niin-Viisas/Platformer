import pygame
import os
from Valikot.paaValikko import paaValikko
from Kentta.kentta import *
from asetukset import *
from asetukset import asetukset
from threading import Thread

# main-funktio

def main():
    # Hakee näytön resoluution asetukset-oliosta
    Setting = asetukset(1)
    lista = Setting.arvot()
    HEIGHT = lista[1]
    WIDTH = lista[2]
    
    #Tausta
    bg = pygame.image.load("pics/Background.png")       #Tämän sijasta voisi olla lista, jotta saadaan kullekkin kentälle oma tausta
    
    #Asettaa ikkunan keskelle näyttöä
    x = (1920-WIDTH)/2
    y = (1080-HEIGHT)/2
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

    # Avaa ikkunan
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    #Kutsuu valikko-oliota
    # valikko = paaValikko(SCREEN, WIDHT, HEIGHT)
    # valikko.main_menu()
    # #Game-Active variaabeli
    # pygame.display.set_caption("Peli")
    # SCREEN.blit(bg, (0, 0))
    valikko = paaValikko(WIDTH, HEIGHT)

    #Kutsuu kentta-oliota
    
    kentta = taso()
    
    # Game-Active variaabeli
    running = True

    #pygame.mixer.init()
    #pygame.mixer.music.load("music/BTD6.mp3", "mp3")
    #pygame.mixer.music.play()

    # Gameloop
    while running:
        # Check For Quit
        # Siirtyy päävalikkoon
        valikko.main_menu()


        # Kutsuu kentan metodia testi, jonka on tarkoitus olla sandbox,
        # jossa voi kokeilla muita luokkia
        kentta.testi()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        


# Kutsutaan main-funktiota
if __name__ == "__main__":
    main()
