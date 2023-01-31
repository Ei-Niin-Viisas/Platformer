import pygame
from Valikot.paaValikko import *


#main-funktio
#sisältää vain turhaa testikoodia
def main():
    print("Toimii")
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    valikko.tulosta()

#    Button()


#Kutsutaan main-funktiota
if __name__ == "__main__":
    pygame.init()
    main()