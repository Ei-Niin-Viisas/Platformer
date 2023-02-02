import pygame, sys
from Valikot.button import *
#from testi2 import WIDTH, HEIGHT

pygame.display.set_caption("Menu")
#BG = pygame.image.load("testi.jpg")

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, testi:str):
        self.sana = testi
        nappi1 = Button(None, [100,100], "nappula", "Arial","black", "white")

    #olion testimetodi
    def tulosta(self):
        print(self.sana)
