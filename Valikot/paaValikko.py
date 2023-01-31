import pygame, sys
from Valikot.button import *
#from testi2 import WIDTH, HEIGHT

SCREEN = pygame.display.set_mode((450, 400))
pygame.display.set_caption("Menu")
#BG = pygame.image.load("testi.jpg")

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, testi:str):
        self.sana = testi

    #olion testimetodi
    def tulosta(self):
        print(self.sana)
