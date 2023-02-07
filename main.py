import pygame, os, time
from Valikot.paaValikko import paaValikko
from Kentta.kentta import *
from asetukset import asetukset
from threading import Thread

#main-funktio
#sisältää vain turhaa testikoodia
def main():
    #Hakee fps:n ja näytön resoluution asetukset-oliosta
    Setting = asetukset(2)
    lista = Setting.arvot()
    FPS = lista[0]
    HEIGHT = lista[1]
    WIDHT = lista[2]
    
    #Asettaa ikkunan keskelle näyttöä
    x = (1920-WIDHT)/2
    y = (1080-HEIGHT)/2
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    
    #Avaa ikkunan
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDHT, HEIGHT))
    
    #Luo kello-olion
    FramePerSec = pygame.time.Clock()
    
    #Kutsuu valikko-oliota
    valikko = paaValikko(SCREEN, WIDHT, HEIGHT)

    #Kutsuu kentta-oliota
    kentta = taso(SCREEN, WIDHT, HEIGHT)


    #Game-Active variaabeli
    running = True


    # Gameloop
    while running:
    #Check For Quit
        #Siirtyy päävalikkoon
        valikko.main_menu()

        #Kutsuu kentan metodia testi, jonka on tarkoitus olla sandbox, 
        #jossa voi kokeilla muita luokkia
        kentta.testi()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        FramePerSec.tick(FPS)
        pygame.display.update()



#Kutsutaan main-funktiota
if __name__ == "__main__":
    main()