import pygame, os, time
from Valikot.paaValikko import paaValikko
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
    
    #Tausta
    bg = pygame.image.load("pics/Background.png")       #Tämän sijasta voisi olla lista, jotta saadaan kullekkin kentälle oma tausta
    
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
    SCREEN.blit(bg, (0, 0))
    
    running = True
    
    # Gameloop
    while running:
    #Check For Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        FramePerSec.tick(FPS)
        print(FPS)
        pygame.display.update()



#Kutsutaan main-funktiota
if __name__ == "__main__":
    main()