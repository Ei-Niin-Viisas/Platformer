import pygame
from Valikot.paaValikko import paaValikko

#main-funktio
#sisältää vain turhaa testikoodia
def main():
    print("Toimii")
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    valikko.tulosta()


#Kutsutaan main-funktiota
if __name__ == "__main__":
    main()