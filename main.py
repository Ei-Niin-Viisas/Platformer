import pygame
from Valikot.paaValikko import paaValikko

def main():
    print("Toimii")
    sana:str = "tuloste"
    valikko = paaValikko(sana)
    valikko.tulosta()


if __name__ == "__main__":
    main()