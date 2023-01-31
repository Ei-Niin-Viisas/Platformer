import pygame
from Valikot.paaValikko import paaValikko
from asetukset import asetukset 


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    Set = asetukset(1)
    FPS = Set.arvot()
    SCREEN = pygame.display.set_mode((450, 400))
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
    pygame.init()
    main()