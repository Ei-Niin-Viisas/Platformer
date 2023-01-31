import pygame, os, time
from Valikot.paaValikko import paaValikko
from asetukset import asetukset 


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    Setting = asetukset(1)
    lista = Setting.arvot()
    FPS = lista[0]
    HEIGHT = lista[1]
    WIDHT = lista[2]
    
    x = (1920-WIDHT)/2
    y = (1080-HEIGHT)/2
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDHT, HEIGHT))
    
    FramePerSec = pygame.time.Clock()
    

    valikko = paaValikko("sana")
    #Game-Active variaabeli
    running = True
    # Gameloop
    while running:
    #Check For Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        FramePerSec.tick(FPS)
        print(FPS)



#Kutsutaan main-funktiota
if __name__ == "__main__":
    #pygame.init()
    main()