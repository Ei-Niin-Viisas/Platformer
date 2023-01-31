import pygame, time
from Valikot.paaValikko import paaValikko


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    FPS = 60
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    FramePerSec = pygame.time.Clock()
    #Game-Active variaabeli
    running = True
    # Gameloop
    while running:
    #Check For Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        FramePerSec.tick(FPS)



#Kutsutaan main-funktiota
if __name__ == "__main__":
    pygame.init()
    main()