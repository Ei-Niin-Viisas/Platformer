import pygame
import os
import sys
import time
from Valikot.paaValikko import paaValikko
from Kentta.kentta import *
from asetukset import *
from asetukset import asetukset
from threading import Thread
from game_data import level_0
from levels import Level

# main-funktio
# sisältää vain turhaa testikoodia


def main():
    # Hakee fps:n ja näytön resoluution asetukset-oliosta
    Setting = asetukset(1)
    lista = Setting.arvot()
    FPS = 60
    HEIGHT = lista[1]
    WIDTH = lista[2]
    
    #Asettaa ikkunan keskelle näyttöä
    x = (1920-WIDTH)/2
    y = (1080-HEIGHT)/2
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

    # Avaa ikkunan
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    #Luo kello-olion
    FPSlukko = pygame.time.Clock()
    
    #Kutsuu valikko-oliota
    valikko = paaValikko(WIDTH, HEIGHT)

    #Kutsuu kentta-oliota
    
    levels = Level(level_0, SCREEN)
    kentta = taso(levels)
    
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
        
        FPSlukko.tick(FPS)
        pygame.display.update()


# Kutsutaan main-funktiota
if __name__ == "__main__":
    main()
