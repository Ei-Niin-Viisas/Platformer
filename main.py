import pygame, os, time
from Valikot.paaValikko import paaValikko
from Kentta.leveli import *
from asetukset import asetukset
from threading import Thread

#main-funktio
#sisältää vain turhaa testikoodia
def main():
    #Hakee fps:n ja näytön resoluution asetukset-oliosta
    Setting = asetukset(1)
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
    valikko.main_menu()
    #Game-Active variaabeli
    pygame.display.set_caption("Peli")
    SCREEN.fill("blue")
    
    running = True

    PT1 = platform()    
    kentta = taso(PT1)


    # Gameloop
    while running:
    #Check For Quit
        SCREEN.fill((0,0,0))
        kentta.testi(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_SPACE:
                        PT1.vaihdaVari()
        
        FramePerSec.tick(FPS)
        #print(FPS)
        pygame.display.update()



#Kutsutaan main-funktiota
if __name__ == "__main__":
    main()