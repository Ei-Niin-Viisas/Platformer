import pygame, sys
from button import Button
from testi2 import WIDTH, HEIGHT

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.png")

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, testi:str):
        self.sana = testi

    #olion testimetodi
    def tulosta(self):
        print(self.sana)

