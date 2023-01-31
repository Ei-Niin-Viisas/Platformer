import pygame
from Valikot.paaValikko import *


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    print("Toimii")
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    valikko.tulosta()

#Game-Active variaabeli
running = True
while running:
# Gameloop

    #Check For Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#    Button()


#Kutsutaan main-funktiota
if __name__ == "__main__":
    pygame.init()
    main()